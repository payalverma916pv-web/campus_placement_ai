import re
from typing import Dict, List

class ResumeParser:
    
    # Email nikalo
    @staticmethod
    def extract_email(text: str) -> str:
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        matches = re.findall(pattern, text)
        return matches[0] if matches else None
    
    # Phone nikalo
    @staticmethod
    def extract_phone(text: str) -> str:
        pattern = r'\b(?:\+91)?[-.\s]?[6789]\d{2}[-.\s]?\d{3,4}[-.\s]?\d{4}\b'
        matches = re.findall(pattern, text)
        return matches[0] if matches else None
    
    # Skills nikalo
    @staticmethod
    def extract_skills(text: str) -> List[str]:
        common_skills = [
            "python", "java", "javascript", "c++", "c#",
            "react", "angular", "vue", "django", "flask", "fastapi",
            "machine learning", "deep learning", "nlp",
            "sql", "mongodb", "postgresql",
            "git", "docker", "aws"
        ]
        text_lower = text.lower()
        found_skills = []
        
        for skill in common_skills:
            if skill in text_lower:
                found_skills.append(skill.title())
        
        return list(set(found_skills))
    
    # Resume parse karo
    @classmethod
    def parse_resume_text(cls, text: str) -> Dict:
        return {
            "email": cls.extract_email(text),
            "phone": cls.extract_phone(text),
            "skills": cls.extract_skills(text),
        }