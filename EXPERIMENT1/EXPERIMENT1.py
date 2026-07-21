import pandas as pd
import json
https://github.com/krishaphobic/EDAPersonalRepo/tree/main
file_path = r"C:\Users\messa\Downloads\Hospital_Patient_Records_encounters.csv"
def extract_single_user(file_path):
    df = pd.read_csv(file_path)
    
    # Isolate the first patient ID found in the repository dataset
    target_user_id = "3de74169-7f67-9304-91d4-757e0f3a14d2"
    user_records = df[df['PATIENT'] == target_user_id]
    
    # Build a simulated user profile schema
    user_profile = {
        "user_id": target_user_id,
        "total_encounters_logged": int(len(user_records)),
        "financial_summary": {
            "total_estimated_cost": round(float(user_records['TOTAL_CLAIM_COST'].sum()), 2),
            "total_insurance_coverage": round(float(user_records['PAYER_COVERAGE'].sum()), 2)
        },
        "recent_encounters": user_records[['START', 'ENCOUNTERCLASS', 'DESCRIPTION']].head(5).to_dict(orient='records')
    }
    
    # Save user to a separate file to track in Git
    output_filename = "test_user_profile.json"
    with open(output_filename, 'w') as f:
        json.dump(user_profile, f, indent=4)
        
    print(f"Created mock user file: '{output_filename}' with {len(user_records)} associated historical logs.")

if __name__ == "__main__":
    extract_single_user(file_path) 
