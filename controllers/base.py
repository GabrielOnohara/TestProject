class BaseResource:
    def get_pagination_params(self, req):
        page_size = req.get_param_as_int('page_size', default=5)
        page_number = req.get_param_as_int('page_number', default=1)

        if page_size <= 0:
            page_size = 5

        if page_number <= 0:
            page_number = 1

        return page_size, page_number
