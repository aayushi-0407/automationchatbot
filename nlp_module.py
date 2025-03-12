import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_parameters(text):
    doc = nlp(text.lower())
    params = {"frequency": None, "bandwidth": None}
    
    # Regex to extract GHz and MHz values
    freq_match = re.search(r"(\d+(\.\d+)?)\s*(ghz|mhz)", text.lower())
    bandwidth_match = re.findall(r"(\d+)\s*mhz", text.lower())

    if freq_match:
        params["frequency"] = freq_match.group(1) + " " + freq_match.group(3)  # Example: 3.6 GHz

    if bandwidth_match:
        params["bandwidth"] = bandwidth_match[0] + " MHz"  # Example: 80 MHz

    return params
