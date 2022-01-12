from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from pprint import pprint

suplier_product_count = [
    ("Amstbase", "tulpin", 10),
    ("Berlinbase", "watermark", 5),
    ("Amstbase", "rose", 3),
    ("Amstbase", "tulpin", 7),
    ("Berlinbase", "pion", 20),
    ("Amstbase", "pion", 5),
]

product_name_by_supplier = defaultdict(list)

for supplier, product, count in suplier_product_count:
    product_name_by_supplier[supplier].append({product: count})

for key, supplier in product_name_by_supplier.items():
    c = Counter()
    for d in supplier:
        c.update(d)
    product_name_by_supplier[key] = dict(c)

for key, supplier in product_name_by_supplier.items():
    print(key,end=':\n')
    bar = OrderedDict(sorted(supplier.items(), key=lambda t: t[0]))
    for product, count in bar.items():
        print(product, ' ', count)