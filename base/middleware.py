from django.http import HttpResponseRedirect
from fortytwo import settings


class CanonicalDomainMiddleware(object):
    pass
    # def process_request(self, request):
    #     if settings.CURRENT_HOST != request.get_host():
    #         return HttpResponseRedirect('%s%s' % (
    #             settings.BASE_URL, request.get_full_path(),
    #         ))