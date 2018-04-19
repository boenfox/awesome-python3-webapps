#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
JSON API definition
'''

import json, logging, inspect, functools

class Page(object):
    '''
    page object for display pages.
    '''

    def __init__(self, item_count, page_index=1, page_size=10):
        '''
        Init Pagination by item_count, page_index and page_size.
        '''
        self.item_count = item_count
        self.page_size = page_size
        self.page_count  = item_count
         

class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional).
    '''

    def __init__(self, error, data='',message=''):
        super(APIError,self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    '''
    Indicate the imput value has error. The data specifis the error field of input form.
    '''

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    '''
    Indicate the resorce was not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message) 


class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden','permission', message)


if __name__=='__main__':
    import doctest
    doctest.testmod()
