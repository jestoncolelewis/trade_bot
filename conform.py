from data_in import reddit, news, history

def combine(src1, src2):
    data = []
    for i in src1:
        if i not in src2:
            data.append(i['symbol'])
    return data

r_data = reddit()

a_data = news()

data = combine(r_data, a_data)

prices = history(data)