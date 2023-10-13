# d = {'result':True, 'values':[1, 2, 3, 4], 'comment':None}

class Json:
    """class json constructor"""
    def __init__(self):
        self.json = {}

    def set_result(self, n=True):
        self.json['result'] = n
        return self
    def set_values(self, n=4):
        results = []
        for val in range(n):
            results.append(val)
        self.json['values'] = results
        return self
    def set_comment(self, n=None):
        self.json['comment'] = n
        return self
    def clean(self):
        self.json.clear()
        return self

# var = Json()
# var.set_result(False).set_values(5).set_comment('Hello')
# print(var.json)
# var.clean()
# print(var.json)