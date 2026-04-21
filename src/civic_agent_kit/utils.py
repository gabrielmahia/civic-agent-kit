"""Utilities for East African civic data."""

KENYA_COUNTIES = [
    "Nairobi", "Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita Taveta",
    "Garissa", "Wajir", "Mandera", "Marsabit", "Isiolo", "Meru", "Tharaka Nithi",
    "Embu", "Kitui", "Machakos", "Makueni", "Nyandarua", "Nyeri", "Kirinyaga",
    "Murang'a", "Kiambu", "Turkana", "West Pokot", "Samburu", "Trans Nzoia",
    "Uasin Gishu", "Elgeyo Marakwet", "Nandi", "Baringo", "Laikipia", "Nakuru",
    "Narok", "Kajiado", "Kericho", "Bomet", "Kakamega", "Vihiga", "Bungoma",
    "Busia", "Siaya", "Kisumu", "Homa Bay", "Migori", "Kisii", "Nyamira",
]

COUNTY_CODES = {name: i + 1 for i, name in enumerate(KENYA_COUNTIES)}

class KenyaCounties:
    all = KENYA_COUNTIES
    codes = COUNTY_CODES

    @classmethod
    def get_code(cls, name: str) -> int | None:
        return cls.codes.get(name.title())

    @classmethod
    def is_valid(cls, name: str) -> bool:
        return name.title() in cls.codes


EN_TO_SW = {
    "county": "kaunti", "budget": "bajeti", "parliament": "bunge",
    "rights": "haki", "water": "maji", "land": "ardhi",
    "health": "afya", "education": "elimu", "drought": "ukame",
    "development": "maendeleo", "government": "serikali",
    "constitution": "katiba", "law": "sheria", "people": "wananchi",
}

class KiswahiliTranslator:
    @staticmethod
    def translate(text: str) -> str:
        result = text.lower()
        for en, sw in EN_TO_SW.items():
            result = result.replace(en, sw)
        return result
