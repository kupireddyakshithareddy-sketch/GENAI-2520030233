
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read values from .env file
input_price = float(os.getenv("INPUT_PRICE"))
output_price = float(os.getenv("OUTPUT_PRICE"))

input_tokens = int(os.getenv("INPUT_TOKENS"))
output_tokens = int(os.getenv("OUTPUT_TOKENS"))

rpm_limit = int(os.getenv("RPM_LIMIT"))
tpm_limit = int(os.getenv("TPM_LIMIT"))

monthly_budget = float(os.getenv("MONTHLY_BUDGET"))

# Calculate token costs
input_cost = (input_tokens / 1000000) * input_price
output_cost = (output_tokens / 1000000) * output_price

total_cost = input_cost + output_cost

# Calculate rate limits
total_tokens = input_tokens + output_tokens

print("\n========== TOKEN BUDGET REPORT ==========")

print("Input Tokens:", input_tokens)
print("Output Tokens:", output_tokens)
print("Total Tokens:", total_tokens)

print("\nInput Cost: $", round(input_cost, 6))
print("Output Cost: $", round(output_cost, 6))
print("Total API Cost: $", round(total_cost, 6))

print("\nMonthly Budget: $", monthly_budget)

if total_cost <= monthly_budget:
    print("Budget Status: Within Budget")
else:
    print("Budget Status: Budget Exceeded")

print("\nRPM Limit:", rpm_limit)
print("TPM Limit:", tpm_limit)

if total_tokens <= tpm_limit:
    print("TPM Status: Within Limit")
else:
    print("TPM Status: Limit Exceeded")

print("\n========== REPORT COMPLETED ==========")
