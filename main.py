# main.py
# This script simulates monitoring social media mentions for potential leads
# and identifying false alarms, reflecting the challenges discussed in the article.

# Simulate social media mentions (example tweets in Turkish)
mentions = [
    "Ürününüz hakkında bilgi alabilir miyim? #destek", # Potential Lead: asking for product info/support
    "Harika bir çekiliş! Katılmak için RT yapın!",     # False Alarm: common social media noise
    "Yeni telefonum için kılıf arıyorum, öneriniz var mı?", # Potential Lead: looking for a product
    "Gününüz güzel geçsin! #mutluluk",                 # Noise: general sentiment, not a lead
    "Hizmet kalitenizden çok memnunum, teşekkürler!", # Potential Lead: positive feedback on service
    "Bu hafta sonu indirimleri kaçırmayın!",           # False Alarm: promotional content
    "Destek ekibinize nasıl ulaşabilirim?",           # Potential Lead: seeking support
    "Takipçi sayımı artırmak istiyorum, karşılıklı takip?", # False Alarm: engagement bait
    "X markasının yeni ürününü denediniz mi?",         # Noise: general discussion, not directly a lead for 'our' product
    "Günün en güzel fotoğrafı! #manzara",             # Noise: irrelevant content
    "Fiyat bilgisi alabilir miyim?",                   # Potential Lead: asking for pricing
    "Şikayetim var, yardımcı olabilir misiniz?",       # Potential Lead: expressing a complaint, needs attention
    "Yeni bir kampanya başlatıyoruz, detaylar için tıklayın!", # False Alarm: promotional content
    "Ürününüzle ilgili bir sorun yaşıyorum.",         # Potential Lead: reporting a product issue
    "Bu bot gerçekten işe yarıyor mu?",               # Potential Lead: asking about a product/service (if 'bot' is our product)
    "Süper indirimler başladı!",                       # False Alarm: promotional content
    "Müşteri hizmetleri numaranız nedir?",             # Potential Lead: seeking customer service
    "Beğen ve kazan kampanyası!",                     # False Alarm: engagement bait/giveaway
    "Hizmetleriniz hakkında daha fazla bilgi istiyorum.", # Potential Lead: seeking more info on services
    "Yeni bir blog yazısı yayınladım, okumak ister misiniz?", # Noise: self-promotion, not a lead
]

# Define keywords that indicate a potential lead
# These are words a business might look for to identify interested customers or issues.
lead_keywords = [
    "ürün", "hizmet", "destek", "şikayet", "sorun", "fiyat",
    "müşteri hizmetleri", "bilgi alabilir miyim", "arıyorum",
    "yardımcı olabilir misiniz", "memnunum", "bot"
]

# Define keywords that indicate a false alarm or irrelevant noise
# These are common social media phrases that are unlikely to be real business leads.
false_alarm_keywords = [
    "çekiliş", "kampanya", "indirim", "takip", "beğen", "rt", "kazan",
    "karşılıklı takip", "mutluluk", "manzara", "blog yazısı", "yayınladım"
]

def classify_mention(mention):
    """
    Classifies a social media mention as a potential lead, false alarm, or noise.
    """
    mention_lower = mention.lower()

    # Check for lead keywords first (higher priority for business)
    for keyword in lead_keywords:
        if keyword in mention_lower:
            return "POTENTIAL_LEAD"
            
    # If not a lead, check for false alarm keywords
    for keyword in false_alarm_keywords:
        if keyword in mention_lower:
            return "FALSE_ALARM"
            
    # If neither, classify as general noise
    return "NOISE"

# Process each mention and categorize it
total_mentions = 0
potential_leads = 0
false_alarms = 0
noise = 0

print("--- Social Media Monitoring Log ---")
for i, mention in enumerate(mentions):
    total_mentions += 1
    classification = classify_mention(mention) # Classification logic applied here
    
    print(f"[{i+1:02d}] '{mention}' -> {classification}")
    
    if classification == "POTENTIAL_LEAD":
        potential_leads += 1
    elif classification == "FALSE_ALARM":
        false_alarms += 1
    else:
        noise += 1

# Display summary results
print("\n--- Monitoring Summary ---")
print(f"Total Mentions Processed: {total_mentions}")
print(f"Identified Potential Leads: {potential_leads}")
print(f"Identified False Alarms: {false_alarms}")
print(f"Unclassified Noise: {noise}")

# Add a note reflecting the article's context
print("\nThis simulation demonstrates the challenge of filtering relevant information from social media noise.")
print("It often results in a high number of false alarms compared to actual leads,")
print("mirroring the experience described in the accompanying article.")
