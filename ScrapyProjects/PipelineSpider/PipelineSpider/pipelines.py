class Above100PriceCheck(object):
    def process_item(self, item, spider):
        try:
            price = float(item['company_price_interaday'])
            if price > 100:
                item['company_price_interaday'] = '>100'
        except:
            pass
        return item;


class Below50PriceCheck(object):
    def process_item(self, item, spider):
        try:
            price = float(item['company_price_interaday'])
            if price < 100:
                item['company_price_interaday'] = '<50'
        except:
            pass
        return item;
