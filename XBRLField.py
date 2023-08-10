"""
    Optimized implementation to fetch a single fact
"""

import edgarRequestHelper
import edgarTickerHelper

import pandas
import os


class XBRLField:
    def __init__(self, ticker):
        self.ticker = ticker
        self.factset = {}
        self.factset['CIK'] = edgarTickerHelper.ticker_mapper(ticker)

    def fetchField(self, field, data_class="us-gaap", units="USD"):
        # Check if field is already in factset
        if field in self.factset:
            return self.factset[field]

        # Fetch field
        fact = edgarRequestHelper.get_concepts(self.factset['CIK'], field, data_class)

        # Check if field exists
        if fact is None:
            return None

        # Add field to factset
        self.factset[field] = fact
        units = fact['units'][units]
        annual_facts = [val for val in units if val["form"] == '10-K']
        df = pandas.DataFrame(annual_facts)

        quarters = [val for val in units if val["form"] == '10-Q']
        df2 = pandas.DataFrame(quarters)

        self.factset[field]['annual'] = df
        self.factset[field]['quarterly'] = df2

        return self.factset[field]