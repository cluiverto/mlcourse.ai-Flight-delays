from sklearn.preprocessing import LabelEncoder,StandardScaler
label_encoding = LabelEncoder()


def clean_alpha(df):
    df.Month = df.Month.str.extract(r"(\d+)")
    df.DayofMonth = df.DayofMonth.str.extract(r"(\d+)")
    df.DayOfWeek = df.DayOfWeek.str.extract(r"(\d+)")


def encode(df):
    df['UniqueCarrier'] = label_encoding.fit_transform(df['UniqueCarrier'])
    df['Origin'] = label_encoding.fit_transform(df['Origin'])
    df['Dest'] = label_encoding.fit_transform(df['Dest'])