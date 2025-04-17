import pandas as pd
import random

# Create sample data
data = [{"id": i, "value": random.randint(1, 100)} for i in range(1000)]
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("input_data.csv", index=False)