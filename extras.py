class Endpoint:
    """A simple Endpoint holder, credit to @ahopkins"""

    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "<Endpoint {}>".format(self.x)


def res_factory(url, methods):
    """Factory method to create Resource like classes to be used with the
    Falcon "extracted" Router.

    Credits: https://github.com/richardolsson/falcon-routing-survey
    """

    class Resource:
        def __init__(self):
            self.url = url

        def __repr__(self):
            return "Resource(%s)" % self.url

    def method(self, req, resp):
        pass

    res = Resource()
    for http_method in methods:
        method_name = "on_" + http_method.lower()
        setattr(res, method_name, method)

    return res
