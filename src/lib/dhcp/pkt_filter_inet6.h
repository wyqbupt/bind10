// Copyright (C) 2013 Internet Systems Consortium, Inc. ("ISC")
//
// Permission to use, copy, modify, and/or distribute this software for any
// purpose with or without fee is hereby granted, provided that the above
// copyright notice and this permission notice appear in all copies.
//
// THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH
// REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
// AND FITNESS.  IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT,
// INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
// LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
// OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
// PERFORMANCE OF THIS SOFTWARE.

#ifndef PKT_FILTER_INET6_H
#define PKT_FILTER_INET6_H

#include <dhcp/pkt_filter6.h>
#include <boost/scoped_array.hpp>

namespace isc {
namespace dhcp {

/// @brief A DHCPv6 packet handling class using datagram sockets.
///
/// This class opens a datagram IPv6/UDPv6 socket. It also implements functions
/// to send and receive DHCPv6 messages through this socket. It is a default
/// class to be used by @c IfaceMgr to access IPv6 sockets.
class PktFilterInet6 : public PktFilter6 {
public:

    /// @brief Constructor.
    ///
    /// Initializes a control buffer used in the message transmission.
    PktFilterInet6();

    /// @brief Opens a socket.
    ///
    /// This function open an IPv6 socket on an interface and binds it to a
    /// specified UDP port and IP address.
    ///
    /// @param iface Interface descriptor.
    /// @param addr Address on the interface to be used to send packets.
    /// @param port Port number.
    /// @param join_multicast A boolean parameter which indicates whether
    /// socket should join All_DHCP_Relay_Agents_and_servers multicast
    /// group.
    ///
    /// @return A structure describing a primary and fallback socket.
    /// @throw isc::dhcp::SocketConfigError if error occured when opening
    /// or configuring a socket.
    virtual SocketInfo openSocket(const Iface& iface,
                                  const isc::asiolink::IOAddress& addr,
                                  const uint16_t port,
                                  const bool join_multicast);

    /// @brief Receives DHCPv6 message on the interface.
    ///
    /// This function receives a single DHCPv6 message through a socket
    /// open on a specified interface. This function will block if there is
    /// no message waiting on the specified socket. Therefore the @c IfaceMgr
    /// must first check that there is any message on the socket (using
    /// select function) prior to calling this function.
    ///
    /// @param socket_info A structure holding socket information.
    ///
    /// @return A pointer to received message.
    /// @throw isc::dhcp::SocketReadError if error occurred during packet
    /// reception.
    virtual Pkt6Ptr receive(const SocketInfo& socket_info);

    /// @brief Sends DHCPv6 message through a specified interface and socket.
    ///
    /// Thie function sends a DHCPv6 message through a specified interface and
    /// socket. In general, there may be multiple sockets open on a single
    /// interface as a single interface may have multiple IPv6 addresses.
    ///
    /// @param iface Interface to be used to send packet.
    /// @param sockfd A socket descriptor
    /// @param pkt A packet to be sent.
    ///
    /// @return A result of sending the message. It is 0 if successful.
    /// @throw isc::dhcp::SocketWriteError if error occured when sending a
    /// packet.
    virtual int send(const Iface& iface, uint16_t sockfd,
                     const Pkt6Ptr& pkt);

private:
    /// Length of the control_buf_ array.
    size_t control_buf_len_;
    /// Control buffer, used in transmission and reception.
    boost::scoped_array<char> control_buf_;
};

} // namespace isc::dhcp
} // namespace isc

#endif // PKT_FILTER_INET6_H
