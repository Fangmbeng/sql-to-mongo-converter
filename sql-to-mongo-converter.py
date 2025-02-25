class SQLToMongo:
    def __init__(self, sql_query):
        self.sql_query = sql_query
        self.parsed_query = {}

    def parse_select(self):
        select_parts = self.sql_query.split('SELECT ')[1].split(' FROM ')[0].split(', ')
        self.parsed_query['projection'] = {field.strip(): 1 for field in select_parts}

    def parse_from(self):
        from_parts = self.sql_query.split(' FROM ')[1].split()
        self.parsed_query['collection'] = from_parts[0].strip()

    def parse_where(self):
        if ' WHERE ' in self.sql_query:
            where_clause = self.sql_query.split(' WHERE ')[1].split(' LIMIT ')[0]
            conditions = where_clause.split(' AND ')
            self.parsed_query['filter'] = {}
            for condition in conditions:
                field, op, value = condition.strip().split(' ', 2)
                if op.upper() == '=':
                    self.parsed_query['filter'][field] = value.strip("'")
                elif op.upper() == 'IN':
                    values = [v.strip() for v in value.strip('()').split(',')]
                    self.parsed_query['filter'][field] = {'$in': values}
                elif op.upper() == 'LIKE':
                    pattern = value.strip("'").replace('%', '.*')
                    self.parsed_query['filter'][field] = {'$regex': f'^{pattern}$'}

    def parse_limit(self):
        if ' LIMIT ' in self.sql_query:
            limit_clause = self.sql_query.split(' LIMIT ')[1]
            self.parsed_query['limit'] = int(limit_clause)

    def convert(self):
        self.parse_select()
        self.parse_from()
        self.parse_where()
        self.parse_limit()
        return self.parsed_query

# Example usage:
sql_query = "SELECT name, age FROM users WHERE active = 'true' AND age IN (20, 30) AND name LIKE 'John%' LIMIT 10"
converter = SQLToMongo(sql_query)
mongo_query = converter.convert()
print(mongo_query)
