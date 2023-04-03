from data_in import reddit, twitter, history

def combine(src1, src2):
    data = []
    for i in src1:
        for j in src2:
            if i['symbol'] != j['symbol']:
                data.append(i)
            else:
                data.append(j)
    return data

r_data = reddit()

t_data = twitter()

data = combine(r_data, t_data)

historic = history(data)