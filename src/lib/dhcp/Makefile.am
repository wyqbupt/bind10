SUBDIRS = . tests

AM_CPPFLAGS = -I$(top_builddir)/src/lib -I$(top_srcdir)/src/lib
AM_CPPFLAGS += $(BOOST_INCLUDES)
AM_CXXFLAGS = $(B10_CXXFLAGS)

# Some versions of GCC warn about some versions of Boost regarding
# missing initializer for members in its posix_time.
# https://svn.boost.org/trac/boost/ticket/3477
# But older GCC compilers don't have the flag.
AM_CXXFLAGS += $(WARNING_NO_MISSING_FIELD_INITIALIZERS_CFLAG)

CLEANFILES = *.gcno *.gcda

lib_LTLIBRARIES = libkea-dhcp++.la
libkea_dhcp___la_SOURCES  =
libkea_dhcp___la_SOURCES += classify.h
libkea_dhcp___la_SOURCES += dhcp6.h dhcp4.h
libkea_dhcp___la_SOURCES += duid.cc duid.h
libkea_dhcp___la_SOURCES += hwaddr.cc hwaddr.h
libkea_dhcp___la_SOURCES += iface_mgr.cc iface_mgr.h
libkea_dhcp___la_SOURCES += iface_mgr_bsd.cc
libkea_dhcp___la_SOURCES += iface_mgr_error_handler.h
libkea_dhcp___la_SOURCES += iface_mgr_linux.cc
libkea_dhcp___la_SOURCES += iface_mgr_sun.cc
libkea_dhcp___la_SOURCES += libdhcp++.cc libdhcp++.h
libkea_dhcp___la_SOURCES += opaque_data_tuple.cc opaque_data_tuple.h
libkea_dhcp___la_SOURCES += option4_addrlst.cc option4_addrlst.h
libkea_dhcp___la_SOURCES += option4_client_fqdn.cc option4_client_fqdn.h
libkea_dhcp___la_SOURCES += option6_ia.cc option6_ia.h
libkea_dhcp___la_SOURCES += option6_iaaddr.cc option6_iaaddr.h
libkea_dhcp___la_SOURCES += option6_iaprefix.cc option6_iaprefix.h
libkea_dhcp___la_SOURCES += option6_addrlst.cc option6_addrlst.h
libkea_dhcp___la_SOURCES += option6_client_fqdn.cc option6_client_fqdn.h
libkea_dhcp___la_SOURCES += option_vendor.cc option_vendor.h
libkea_dhcp___la_SOURCES += option_vendor_class.cc option_vendor_class.h
libkea_dhcp___la_SOURCES += option_int.h
libkea_dhcp___la_SOURCES += option_int_array.h
libkea_dhcp___la_SOURCES += option.cc option.h
libkea_dhcp___la_SOURCES += option_custom.cc option_custom.h
libkea_dhcp___la_SOURCES += option_data_types.cc option_data_types.h
libkea_dhcp___la_SOURCES += option_definition.cc option_definition.h
libkea_dhcp___la_SOURCES += option_space.cc option_space.h
libkea_dhcp___la_SOURCES += option_string.cc option_string.h
libkea_dhcp___la_SOURCES += protocol_util.cc protocol_util.h
libkea_dhcp___la_SOURCES += pkt6.cc pkt6.h
libkea_dhcp___la_SOURCES += pkt4.cc pkt4.h
libkea_dhcp___la_SOURCES += pkt_filter.h pkt_filter.cc
libkea_dhcp___la_SOURCES += pkt_filter6.h pkt_filter6.cc
libkea_dhcp___la_SOURCES += pkt_filter_inet.cc pkt_filter_inet.h
libkea_dhcp___la_SOURCES += pkt_filter_inet6.cc pkt_filter_inet6.h

if OS_LINUX
libkea_dhcp___la_SOURCES += pkt_filter_lpf.cc pkt_filter_lpf.h
endif

libkea_dhcp___la_SOURCES += std_option_defs.h
libkea_dhcp___la_SOURCES += docsis3_option_defs.h

libkea_dhcp___la_CXXFLAGS = $(AM_CXXFLAGS)
libkea_dhcp___la_CPPFLAGS = $(AM_CPPFLAGS) $(LOG4CPLUS_INCLUDES)
libkea_dhcp___la_LIBADD   = $(top_builddir)/src/lib/asiolink/libkea-asiolink.la
libkea_dhcp___la_LIBADD  += $(top_builddir)/src/lib/dns/libkea-dns++.la
libkea_dhcp___la_LIBADD  += $(top_builddir)/src/lib/util/libkea-util.la
libkea_dhcp___la_LDFLAGS  = -no-undefined -version-info 2:0:0

EXTRA_DIST  = README libdhcp++.dox

# Specify the headers for copying into the installation directory tree. User-
# written libraries may need access to all libdhcp++ headers.
libkea_dhcp___includedir = $(pkgincludedir)/dhcp
libkea_dhcp___include_HEADERS = \
    classify.h \
    dhcp4.h \
    dhcp6.h \
    duid.h \
    hwaddr.h \
    iface_mgr.h \
    libdhcp++.h \
    option.h \
    option4_addrlst.h \
    option6_addrlst.h \
    option6_ia.h \
    option6_iaaddr.h \
    option_custom.h \
    option_data_types.h \
    option_definition.h \
    option_int.h \
    option_int_array.h \
    option_space.h \
    option_string.h \
    pkt4.h \
    pkt6.h \
    pkt_filter.h \
    pkt_filter_inet.h \
    pkt_filter_lpf.h \
    protocol_util.h \
    std_option_defs.h

if USE_CLANGPP
# Disable unused parameter warning caused by some of the
# Boost headers when compiling with clang.
libkea_dhcp___la_CXXFLAGS += -Wno-unused-parameter
endif
