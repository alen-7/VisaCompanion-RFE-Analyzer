def analyze_text(text):
    """Enhanced EB-1A risk detection"""
    risks = []
    text_lower = text.lower()
    
    # Criteria-specific checks
    criteria = {
        "Original Contributions": {
            "keywords": ["original", "innovative", "breakthrough"],
            "required": ["patent", "citation", "adopted by"],
            "risk": "High"
        },
        "Publications": {
            "keywords": ["published", "paper", "article"],
            "required": ["peer-reviewed", "journal", "impact factor"],
            "risk": "Medium"
        },
        "Critical Role": {
            "keywords": ["critical", "essential", "lead"],
            "required": ["testimonial", "organization chart", "official document"],
            "risk": "High"
        }
    }

    for criterion, config in criteria.items():
        # Check for keywords
        found_kw = any(kw in text_lower for kw in config["keywords"])
        found_req = any(req in text_lower for req in config["required"])
        
        if not found_kw:
            risks.append((criterion, f"No mention of {criterion.lower()}", "High"))
        elif not found_req:
            risks.append((criterion, f"Lacks independent evidence for {criterion.lower()}", config["risk"]))
    
    # Subjective language detection
    subjective_phrases = [
        ("world-class", "Medium"),
        ("unparalleled", "Medium"), 
        ("top expert", "Medium"),
        ("very talented", "Low")
    ]
    
    for phrase, severity in subjective_phrases:
        if phrase in text_lower:
            risks.append(("Subjective Language", f"Avoid subjective term: '{phrase}'", severity))
    
    return risks