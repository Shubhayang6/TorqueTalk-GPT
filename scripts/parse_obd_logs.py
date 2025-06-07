import json
import re
from pathlib import Path

def parse_obd_logs(file_path: str, output_path: str = "data/parsed_obd.json"):
    """
    Parses the raw OBD-II logs and extracts fault codes with description.
    Saves structured JSON to the given output path.
    """
    
    pattern = re.compile(r"(P\d{4})")  # match standard OBD-II codes
    parsed = []
    
    with open(file_path, "r") as infile:
        for line in infile:
            match = pattern.search(line)
            if match:
                parsed.append({
                    "code": match.group(1),
                    "description": line.strip()
                })
                
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as outfile:
        json.dump(parsed, outfile, indent=2)
        
    print(f"Parsed {len(parsed)} fault codes savedd to {output_path}")
    
    
if __name__ == "__main__":
    parse_obd_logs("data/sample_log.txt")