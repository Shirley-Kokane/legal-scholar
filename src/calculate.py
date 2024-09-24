from enum import Enum
import yaml
import google.generativeai as genai
import os


class Embed:
    def __init__(self) -> None:
        pass

    def embed_single_text(self, text: str):
        raise NotImplementedError("")

    def embed_multiple_documents(self, content: list[str]):
        raise NotImplementedError("")


class ModelType(Enum):
    HUGGING_FACE = "hugging_face"
    SENTENCE_TRANSFORMER = "sentence_transformer"
    OPENAI = "openai"
    GEMINI = "gemini"


class Config:
    def __init__(self, filepath) -> None:
        with open(filepath) as stream:
            config = yaml.safe_load(stream)

        main_config = config["main_config"]
        self.batch_size = main_config["batch_size"]
        self.model_name = main_config["model_name"]

        model_config = config[self.model_name]
        self.context_length = model_config["context_length"]
        self.chunk_size = model_config["chunk_size"]
        self.chunk_overlap = model_config["chunk_overlap"]
        self.embedding_size = model_config["embedding_size"]
        for model_type in ModelType:
            if model_type.value == model_config["model_type"]:
                self.model_type = model_type
                break

        assert hasattr(self, "model_type"), f"Unsupported model type {model_type}"

        for key in ["context_length", "chunk_size", "chunk_overlap"]:
            if key in main_config:
                setattr(self, key, main_config[key])

        self.max_seq_len = self.context_length
        if "max_seq_len" in model_config:
            self.max_seq_len = min(self.context_length, model_config["max_seq_len"])

class GeminiEmbed(Embed):
    def __init__(self, config: Config) -> None:
        super().__init__()
        # genai.configure(api_key="")

        supported_models = [
            m.name
            for m in genai.list_models()
            if "embedContent" in m.supported_generation_methods
        ]

        assert config.model_name in supported_models
        self.model_name = config.model_name

    def embed_single_text(self, text: str):
        embedding = genai.embed_content(
            model=self.model_name,
            content=text,
            task_type="retrieval_document",
            title=None,
        )
        return embedding["embedding"]

    def embed_multiple_documents(self, content: list[str]):

        embeddings = []
        for sample in content:
            embedding = genai.embed_content(
                model=self.model_name,
                content=sample,
                task_type="retrieval_document",
                title=None,
            )
            embeddings.append(embedding["embedding"])

        return embeddings
    
