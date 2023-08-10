import edgarRequestHelper as edgarRequestHelper
import edgarTickerHelper as edgarTickerHelper


TICKER = "NPK"

# Get CIK
CIK = edgarTickerHelper.ticker_mapper(TICKER)

netIncomeLoss = edgarRequestHelper.get_concepts(CIK, "NetIncomeLoss")

annual_results = {}
for entry in netIncomeLoss["units"]["USD"]:
    if entry["fp"]=="FY":
        annual_results[entry["fy"]] = entry["val"]

print(annual_results)

