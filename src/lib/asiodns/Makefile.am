SUBDIRS = . tests

AM_CPPFLAGS = -I$(top_srcdir)/src/lib -I$(top_builddir)/src/lib
AM_CPPFLAGS += $(BOOST_INCLUDES)
AM_CPPFLAGS += -I$(top_srcdir)/src/lib/dns -I$(top_builddir)/src/lib/dns
AM_CPPFLAGS += -I$(top_srcdir)/src/lib/asiolink -I$(top_builddir)/src/lib/asiolink
AM_CPPFLAGS += -I$(top_srcdir)/src/lib/util -I$(top_builddir)/src/lib/util

AM_CXXFLAGS = $(B10_CXXFLAGS)

CLEANFILES = *.gcno *.gcda asiodef.h asiodef.cc

# Define rule to build logging source files from message file
asiodef.h asiodef.cc: asiodef.mes
	$(top_builddir)/src/lib/log/compiler/message $(top_srcdir)/src/lib/asiodns/asiodef.mes

BUILT_SOURCES = asiodef.h asiodef.cc

lib_LTLIBRARIES = libasiodns.la
libasiodns_la_SOURCES = dns_answer.h
libasiodns_la_SOURCES += asiodns.h
libasiodns_la_SOURCES += dns_lookup.h
libasiodns_la_SOURCES += dns_server.h
libasiodns_la_SOURCES += dns_service.cc dns_service.h
libasiodns_la_SOURCES += tcp_server.cc tcp_server.h
libasiodns_la_SOURCES += udp_server.cc udp_server.h
libasiodns_la_SOURCES += io_fetch.cc io_fetch.h

nodist_libasiodns_la_SOURCES = asiodef.cc asiodef.h

EXTRA_DIST = asiodef.mes

# Note: the ordering matters: -Wno-... must follow -Wextra (defined in
# B10_CXXFLAGS)
libasiodns_la_CXXFLAGS = $(AM_CXXFLAGS)
if USE_CLANGPP
# Same for clang++, but we need to turn off -Werror completely.
libasiodns_la_CXXFLAGS += -Wno-error
endif
libasiodns_la_CPPFLAGS = $(AM_CPPFLAGS)
libasiodns_la_LIBADD = $(top_builddir)/src/lib/log/liblog.la