import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def generate_audit_report(data):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "❌ Error: API Key missing."

    genai.configure(api_key=api_key)

    try:
        # Latest model pick cheddham
        model = genai.GenerativeModel('gemini-1.5-flash') 
        
        # Kevalam top 3 high risk rows mathrame pampiddham (Quota save avthundi)
        high_risk_data = data[data['Risk_Level'] == 'High'].head(3)
        
        # Columns thagginchadam (Telling AI only essential info)
        if not high_risk_data.empty:
            summary_data = high_risk_data[['Amount', 'Risk_Level']].to_string()
        else:
            return "✅ No High-Risk transactions found to analyze."

        prompt = f"Summarize these 3 suspicious audit transactions in 2 lines:\n{summary_data}"
        
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        if "429" in str(e):
            return "⚠️ Quota Full: Please wait 60 seconds and try again."
        return f"❌ AI Connection Error: {str(e)}"