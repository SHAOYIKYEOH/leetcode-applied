import pandas as pd
from fizzbuzz_solution import performance

dataset = pd.DataFrame({'target':[100,100,100],'score':[80,60,30]})

result = performance(dataset)
print(result)