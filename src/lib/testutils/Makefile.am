SUBDIRS = . testdata

AM_CPPFLAGS = -I$(top_srcdir)/src/lib -I$(top_builddir)/src/lib
AM_CPPFLAGS += $(BOOST_INCLUDES)
AM_CXXFLAGS=$(B10_CXXFLAGS)

if HAVE_GTEST
noinst_LTLIBRARIES = libkea-testutils.la

libkea_testutils_la_SOURCES = srv_test.h srv_test.cc
libkea_testutils_la_SOURCES += dnsmessage_test.h dnsmessage_test.cc
libkea_testutils_la_SOURCES += mockups.h
libkea_testutils_la_CPPFLAGS = $(AM_CPPFLAGS) $(GTEST_INCLUDES)
libkea_testutils_la_LIBADD  = $(top_builddir)/src/lib/asiolink/libkea-asiolink.la
libkea_testutils_la_LIBADD += $(top_builddir)/src/lib/dns/libkea-dns++.la
endif

EXTRA_DIST = portconfig.h socket_request.h
