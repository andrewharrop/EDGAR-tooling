import edgarRequestHelper as edgarRequestHelper
import edgarTickerMapper as edgarTickerMapper


TICKER = "NPK"

# Get CIK
CIK = edgarTickerMapper.ticker_mapper(TICKER)

netIncomeLoss = edgarRequestHelper.get_concepts(CIK, "NetIncomeLoss")

annual_results = {}
for entry in netIncomeLoss["units"]["USD"]:
    if entry["fp"]=="FY":
        annual_results[entry["fy"]] = entry["val"]

print(annual_results)

