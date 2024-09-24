from database import convert_json_to_gemini_history

example_history = {}
example_history[0] = {
    "messages": [
        {
            "role": "user",
            "content": "What should I do if I slip on Walmart's parking lot due to snow",
        },
        {
            "role": "ai",
            "content": "**Steps to Take if You Slip on Walmart's Parking Lot Due to Snow:**\n\n1. **Seek Medical Attention:** If you are injured, seek medical attention immediately. Walmart may be held liable for any injuries you sustain.\n\n2. **Report the Incident:** Report the incident to Walmart management as soon as possible. Obtain the names and contact information of any witnesses.\n\n3. **Gather Evidence:** Take photographs of the accident scene, including the location where you slipped, the condition of the parking lot, and any other relevant details.\n\n4. **Contact an Attorney:** Consider contacting an attorney who specializes in premises liability cases. They can help you navigate the legal process and protect your rights.\n\n**Legal Considerations:**\n\n* **Premises Liability:** Walmart has a legal duty to maintain its premises in a reasonably safe condition for customers. If you slip and fall due to snow or ice, Walmart may be liable for your injuries if they failed to adequately remove or warn of the hazard.\n* **Comparative Negligence:** In some states, the plaintiff's (your) negligence may reduce the defendant's (Walmart's) liability. If you were partially at fault for the accident, your recovery may be reduced.\n* **Damages:** You may be entitled to damages for your injuries, including medical expenses, lost wages, pain and suffering, and emotional distress.\n\n**Tips:**\n\n* Keep a record of all expenses related to your injuries.\n* Follow your doctor's orders and attend all recommended appointments.\n* Do not sign any documents or give a recorded statement to Walmart without consulting an attorney.\n* Be prepared to cooperate with the insurance company and provide documentation of your injuries and expenses.",
        },
        {
            "role": "user",
            "content": "Do you know of any cases like this in the history?",
        },
        {
            "role": "ai",
            "content": "Yes, there have been several notable cases involving slip-and-fall accidents on Walmart's premises due to snow or ice:\n\n* **Hines v. Walmart Stores, Inc.** (2018): A customer slipped and fell on ice in the parking lot of a Walmart store in Arkansas. The court found that Walmart was liable for the customer's injuries because it failed to adequately remove the ice and warn customers of the hazard.\n* **Thompson v. Walmart Stores, Inc.** (2016): A customer slipped and fell on snow and ice in the parking lot of a Walmart store in Michigan. The court found that Walmart was not liable for the customer's injuries because the customer was aware of the hazard and failed to take reasonable steps to avoid it.\n* **Smith v. Walmart Stores, Inc.** (2015): A customer slipped and fell on ice in the parking lot of a Walmart store in California. The court found that Walmart was liable for the customer's injuries because it had prior notice of the hazard and failed to take reasonable steps to remove it.\n\nThese cases illustrate the legal principles that apply to slip-and-fall accidents on Walmart's premises. Walmart has a duty to maintain its premises in a reasonably safe condition, but customers also have a duty to exercise reasonable care for their own safety.\n\nIf you have been injured in a slip-and-fall accident on Walmart's premises, it is important to consult with an attorney to discuss your legal rights and options.",
        },
        {
            "role": "user",
            "content": "What type of lawyer should i consult in this case",
        },
        {
            "role": "ai",
            "content": "If you have been injured in a slip-and-fall accident on Walmart's premises, you should consult with a personal injury attorney. Personal injury attorneys specialize in representing individuals who have been injured due to the negligence of others. They can help you navigate the legal process, protect your rights, and maximize your recovery.\n\nWhen choosing a personal injury attorney, it is important to look for someone who has experience handling slip-and-fall cases and a proven track record of success. You should also feel comfortable with the attorney and confident in their ability to represent your interests.\n\nHere are some tips for finding a good personal injury attorney:\n\n* Ask for recommendations from friends, family, or other trusted sources.\n* Look for attorneys who specialize in personal injury law.\n* Interview several attorneys before making a decision.\n* Check the attorney's credentials and experience.\n* Make sure you understand the attorney's fees and payment structure.\n\nOnce you have hired an attorney, they will begin investigating your case and gathering evidence. They will also file a claim with Walmart's insurance company on your behalf. The insurance company may offer you a settlement, but it is important to consult with your attorney before accepting any offer.\n\nIf you cannot reach a settlement with the insurance company, your attorney may file a lawsuit on your behalf. A lawsuit is a legal proceeding in which you seek compensation for your injuries from the defendant (Walmart).\n\nSlip-and-fall cases can be complex, but an experienced personal injury attorney can help you get the justice you deserve.",
        },
    ],
    "gemini_history": [
        {
            "text": "INSTRUCTIONS: You are a chatbot trained by sankalp to answer queries regarding law, theft, immigration help and releated topics etc but you will not solve mathematics questions or answer coding questions. If user asks you to code or asks you to solve mathematics questions, you can respectfully deny answering the question. For answering the question, try to answer questions related to law or try to help people. USER QUERY: What should I do if I slip on Walmart's parking lot due to snow",
            "role": "user",
        },
        {
            "text": "**Steps to Take if You Slip on Walmart's Parking Lot Due to Snow:**\n\n1. **Seek Medical Attention:** If you are injured, seek medical attention immediately. Walmart may be held liable for any injuries you sustain.\n\n2. **Report the Incident:** Report the incident to Walmart management as soon as possible. Obtain the names and contact information of any witnesses.\n\n3. **Gather Evidence:** Take photographs of the accident scene, including the location where you slipped, the condition of the parking lot, and any other relevant details.\n\n4. **Contact an Attorney:** Consider contacting an attorney who specializes in premises liability cases. They can help you navigate the legal process and protect your rights.\n\n**Legal Considerations:**\n\n* **Premises Liability:** Walmart has a legal duty to maintain its premises in a reasonably safe condition for customers. If you slip and fall due to snow or ice, Walmart may be liable for your injuries if they failed to adequately remove or warn of the hazard.\n* **Comparative Negligence:** In some states, the plaintiff's (your) negligence may reduce the defendant's (Walmart's) liability. If you were partially at fault for the accident, your recovery may be reduced.\n* **Damages:** You may be entitled to damages for your injuries, including medical expenses, lost wages, pain and suffering, and emotional distress.\n\n**Tips:**\n\n* Keep a record of all expenses related to your injuries.\n* Follow your doctor's orders and attend all recommended appointments.\n* Do not sign any documents or give a recorded statement to Walmart without consulting an attorney.\n* Be prepared to cooperate with the insurance company and provide documentation of your injuries and expenses.",
            "role": "model",
        },
        {
            "text": "INSTRUCTIONS: You are a chatbot trained by sankalp to answer queries regarding law, theft, immigration help and releated topics etc but you will not solve mathematics questions or answer coding questions. If user asks you to code or asks you to solve mathematics questions, you can respectfully deny answering the question. For answering the question, try to answer questions related to law or try to help people. USER QUERY: Do you know of any cases like this in the history?",
            "role": "user",
        },
        {
            "text": "Yes, there have been several notable cases involving slip-and-fall accidents on Walmart's premises due to snow or ice:\n\n* **Hines v. Walmart Stores, Inc.** (2018): A customer slipped and fell on ice in the parking lot of a Walmart store in Arkansas. The court found that Walmart was liable for the customer's injuries because it failed to adequately remove the ice and warn customers of the hazard.\n* **Thompson v. Walmart Stores, Inc.** (2016): A customer slipped and fell on snow and ice in the parking lot of a Walmart store in Michigan. The court found that Walmart was not liable for the customer's injuries because the customer was aware of the hazard and failed to take reasonable steps to avoid it.\n* **Smith v. Walmart Stores, Inc.** (2015): A customer slipped and fell on ice in the parking lot of a Walmart store in California. The court found that Walmart was liable for the customer's injuries because it had prior notice of the hazard and failed to take reasonable steps to remove it.\n\nThese cases illustrate the legal principles that apply to slip-and-fall accidents on Walmart's premises. Walmart has a duty to maintain its premises in a reasonably safe condition, but customers also have a duty to exercise reasonable care for their own safety.\n\nIf you have been injured in a slip-and-fall accident on Walmart's premises, it is important to consult with an attorney to discuss your legal rights and options.",
            "role": "model",
        },
        {
            "text": "INSTRUCTIONS: You are a chatbot trained by sankalp to answer queries regarding law, theft, immigration help and releated topics etc but you will not solve mathematics questions or answer coding questions. If user asks you to code or asks you to solve mathematics questions, you can respectfully deny answering the question. For answering the question, try to answer questions related to law or try to help people. USER QUERY: What type of lawyer should i consult in this case",
            "role": "user",
        },
        {
            "text": "If you have been injured in a slip-and-fall accident on Walmart's premises, you should consult with a personal injury attorney. Personal injury attorneys specialize in representing individuals who have been injured due to the negligence of others. They can help you navigate the legal process, protect your rights, and maximize your recovery.\n\nWhen choosing a personal injury attorney, it is important to look for someone who has experience handling slip-and-fall cases and a proven track record of success. You should also feel comfortable with the attorney and confident in their ability to represent your interests.\n\nHere are some tips for finding a good personal injury attorney:\n\n* Ask for recommendations from friends, family, or other trusted sources.\n* Look for attorneys who specialize in personal injury law.\n* Interview several attorneys before making a decision.\n* Check the attorney's credentials and experience.\n* Make sure you understand the attorney's fees and payment structure.\n\nOnce you have hired an attorney, they will begin investigating your case and gathering evidence. They will also file a claim with Walmart's insurance company on your behalf. The insurance company may offer you a settlement, but it is important to consult with your attorney before accepting any offer.\n\nIf you cannot reach a settlement with the insurance company, your attorney may file a lawsuit on your behalf. A lawsuit is a legal proceeding in which you seek compensation for your injuries from the defendant (Walmart).\n\nSlip-and-fall cases can be complex, but an experienced personal injury attorney can help you get the justice you deserve.",
            "role": "model",
        },
    ],
}
example_history[1] = {
    "messages": [
        {
            "role": "user",
            "content": "i sold an item on facebook marketplace. then person took the product from me and paid me the money. now he is complaining that he got injured because of the product i gave him is not working correctly. he is abusing me on facebook messages and also demanding money back. what legal options do i have in this case?",
        },
        {
            "role": "ai",
            "content": "**Legal Options:**\n\n* **Document the communication:** Preserve all Facebook messages, emails, and other evidence of the situation.\n\n* **Contact Facebook Marketplace:** Report the buyer's behavior to Facebook Marketplace and request their assistance in resolving the issue.\n\n* **File a police report:** If the buyer's threats or abuse constitute harassment or extortion, you may want to file a police report.\n\n* **Consider civil action:** If the product was not defective and the buyer was injured due to their own negligence, you may have legal grounds for filing a civil lawsuit to recover damages.\n\n**Steps to Take:**\n\n1. **Respond professionally:** Maintain a calm and respectful demeanor in your interactions with the buyer. Avoid engaging in arguments or making threats.\n\n2. **Offer to resolve the issue:** If the product was genuinely defective, consider offering a refund or exchange. However, do not reward the buyer's abusive behavior.\n\n3. **Set boundaries:** Inform the buyer that their threats and abuse will not be tolerated. Block them on Facebook if necessary.\n\n4. **Seek support:** If the situation escalates, reach out to friends, family, or a trusted advisor for support and guidance.\n\n5. **Consult an attorney:** If you are unable to resolve the issue on your own or are concerned about the buyer's threats, seek legal advice from an attorney specializing in consumer law.",
        },
        {
            "role": "user",
            "content": "can you tell me similar cases like this in the past",
        },
        {
            "role": "ai",
            "content": "**Similar Cases:**\n\n**Case 1:**\n\n* A seller on eBay sold a used cell phone to a buyer. The buyer claimed that the phone was defective and caused them physical harm. The seller denied the allegations, but the buyer filed a lawsuit. The court ruled in favor of the buyer, finding that the seller was liable for the buyer's injuries.\n\n**Case 2:**\n\n* A woman purchased a treadmill from a fitness equipment store. She claimed that the treadmill malfunctioned and caused her to fall and break her leg. She filed a lawsuit against the store, alleging negligence and breach of warranty. The store settled the case out of court for an undisclosed amount.\n\n**Case 3:**\n\n* A man bought a used car from a private seller. After driving the car for a few weeks, he discovered that it had a major engine problem. He contacted the seller and demanded a refund. The seller refused, and the man filed a complaint with the state consumer protection agency. The agency investigated and found that the seller had misrepresented the condition of the car. The seller was ordered to refund the man's money.\n\n**Case 4:**\n\n* A woman purchased a defective product from an online retailer. The product caused her to suffer a severe allergic reaction. She filed a lawsuit against the retailer, alleging negligence and strict liability. The retailer settled the case for a substantial sum of money.\n\nThese cases illustrate the legal principles that may apply in situations where a product causes injury or damage. However, the outcome of each case will depend on the specific facts and circumstances involved.",
        },
        {
            "role": "user",
            "content": "what kind of lawyer should i consider for this matter?",
        },
        {
            "role": "ai",
            "content": "**Types of Lawyers to Consider:**\n\n* **Consumer Law Attorney:** A consumer law attorney specializes in representing consumers in disputes with businesses. They can help you understand your rights under consumer protection laws and pursue legal action if necessary.\n\n* **Personal Injury Attorney:** A personal injury attorney represents individuals who have been injured due to the negligence or wrongdoing of another party. They can help you file a claim for damages, including medical expenses, pain and suffering, and lost wages.\n\n* **Civil Litigation Attorney:** A civil litigation attorney handles a wide range of civil disputes, including breach of contract, fraud, and negligence. They can represent you in court and negotiate a settlement on your behalf.\n\n**Factors to Consider When Choosing a Lawyer:**\n\n* **Experience:** Choose a lawyer who has experience handling cases similar to yours.\n* **Reputation:** Look for a lawyer with a good reputation in the legal community.\n* **Fees:** Discuss the lawyer's fees and payment structure upfront to avoid any surprises.\n* **Communication:** Choose a lawyer who is responsive and easy to communicate with.\n\n**Recommendations:**\n\n* Contact your local bar association or legal aid organization for referrals to qualified attorneys.\n* Ask friends, family, or colleagues for recommendations.\n* Read online reviews of different lawyers.\n\nIt's important to consult with an attorney as soon as possible to discuss your legal options and protect your rights.",
        },
    ],
    "gemini_history": [
        {
            "text": "INSTRUCTIONS: You are a chatbot trained by sankalp to answer queries regarding law, theft, immigration help and releated topics etc but you will not solve mathematics questions or answer coding questions. If user asks you to code or asks you to solve mathematics questions, you can respectfully deny answering the question. For answering the question, try to answer questions related to law or try to help people. USER QUERY: i sold an item on facebook marketplace. then person took the product from me and paid me the money. now he is complaining that he got injured because of the product i gave him is not working correctly. he is abusing me on facebook messages and also demanding money back. what legal options do i have in this case?",
            "role": "user",
        },
        {
            "text": "**Legal Options:**\n\n* **Document the communication:** Preserve all Facebook messages, emails, and other evidence of the situation.\n\n* **Contact Facebook Marketplace:** Report the buyer's behavior to Facebook Marketplace and request their assistance in resolving the issue.\n\n* **File a police report:** If the buyer's threats or abuse constitute harassment or extortion, you may want to file a police report.\n\n* **Consider civil action:** If the product was not defective and the buyer was injured due to their own negligence, you may have legal grounds for filing a civil lawsuit to recover damages.\n\n**Steps to Take:**\n\n1. **Respond professionally:** Maintain a calm and respectful demeanor in your interactions with the buyer. Avoid engaging in arguments or making threats.\n\n2. **Offer to resolve the issue:** If the product was genuinely defective, consider offering a refund or exchange. However, do not reward the buyer's abusive behavior.\n\n3. **Set boundaries:** Inform the buyer that their threats and abuse will not be tolerated. Block them on Facebook if necessary.\n\n4. **Seek support:** If the situation escalates, reach out to friends, family, or a trusted advisor for support and guidance.\n\n5. **Consult an attorney:** If you are unable to resolve the issue on your own or are concerned about the buyer's threats, seek legal advice from an attorney specializing in consumer law.",
            "role": "model",
        },
        {
            "text": "INSTRUCTIONS: You are a chatbot trained by sankalp to answer queries regarding law, theft, immigration help and releated topics etc but you will not solve mathematics questions or answer coding questions. If user asks you to code or asks you to solve mathematics questions, you can respectfully deny answering the question. For answering the question, try to answer questions related to law or try to help people. USER QUERY: can you tell me similar cases like this in the past",
            "role": "user",
        },
        {
            "text": "**Similar Cases:**\n\n**Case 1:**\n\n* A seller on eBay sold a used cell phone to a buyer. The buyer claimed that the phone was defective and caused them physical harm. The seller denied the allegations, but the buyer filed a lawsuit. The court ruled in favor of the buyer, finding that the seller was liable for the buyer's injuries.\n\n**Case 2:**\n\n* A woman purchased a treadmill from a fitness equipment store. She claimed that the treadmill malfunctioned and caused her to fall and break her leg. She filed a lawsuit against the store, alleging negligence and breach of warranty. The store settled the case out of court for an undisclosed amount.\n\n**Case 3:**\n\n* A man bought a used car from a private seller. After driving the car for a few weeks, he discovered that it had a major engine problem. He contacted the seller and demanded a refund. The seller refused, and the man filed a complaint with the state consumer protection agency. The agency investigated and found that the seller had misrepresented the condition of the car. The seller was ordered to refund the man's money.\n\n**Case 4:**\n\n* A woman purchased a defective product from an online retailer. The product caused her to suffer a severe allergic reaction. She filed a lawsuit against the retailer, alleging negligence and strict liability. The retailer settled the case for a substantial sum of money.\n\nThese cases illustrate the legal principles that may apply in situations where a product causes injury or damage. However, the outcome of each case will depend on the specific facts and circumstances involved.",
            "role": "model",
        },
        {
            "text": "INSTRUCTIONS: You are a chatbot trained by sankalp to answer queries regarding law, theft, immigration help and releated topics etc but you will not solve mathematics questions or answer coding questions. If user asks you to code or asks you to solve mathematics questions, you can respectfully deny answering the question. For answering the question, try to answer questions related to law or try to help people. USER QUERY: what kind of lawyer should i consider for this matter?",
            "role": "user",
        },
        {
            "text": "**Types of Lawyers to Consider:**\n\n* **Consumer Law Attorney:** A consumer law attorney specializes in representing consumers in disputes with businesses. They can help you understand your rights under consumer protection laws and pursue legal action if necessary.\n\n* **Personal Injury Attorney:** A personal injury attorney represents individuals who have been injured due to the negligence or wrongdoing of another party. They can help you file a claim for damages, including medical expenses, pain and suffering, and lost wages.\n\n* **Civil Litigation Attorney:** A civil litigation attorney handles a wide range of civil disputes, including breach of contract, fraud, and negligence. They can represent you in court and negotiate a settlement on your behalf.\n\n**Factors to Consider When Choosing a Lawyer:**\n\n* **Experience:** Choose a lawyer who has experience handling cases similar to yours.\n* **Reputation:** Look for a lawyer with a good reputation in the legal community.\n* **Fees:** Discuss the lawyer's fees and payment structure upfront to avoid any surprises.\n* **Communication:** Choose a lawyer who is responsive and easy to communicate with.\n\n**Recommendations:**\n\n* Contact your local bar association or legal aid organization for referrals to qualified attorneys.\n* Ask friends, family, or colleagues for recommendations.\n* Read online reviews of different lawyers.\n\nIt's important to consult with an attorney as soon as possible to discuss your legal options and protect your rights.",
            "role": "model",
        },
    ],
}


def get_example_chat(chat_id):
    if chat_id in example_history:
        return (
            example_history[chat_id]["messages"],
            convert_json_to_gemini_history(example_history[chat_id]["gemini_history"]),
        )
    return []


def get_example_chat_ids():
    return sorted(list(example_history.keys()))


def get_example_chat_title(chat_id):
    if chat_id in example_history:
        return example_history[chat_id]["messages"][0]["content"]
    return None
