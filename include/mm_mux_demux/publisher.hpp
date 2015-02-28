/**
 * @file /mm_mux_demux/include/mm_mux_demux/publisher.hpp
 * 
 * @brief Short description of this file.
 **/
/*****************************************************************************
** Ifdefs
*****************************************************************************/

#ifndef mm_mux_demux_PUBLISHER_HPP_
#define mm_mux_demux_PUBLISHER_HPP_

/*****************************************************************************
** Includes
*****************************************************************************/

#include <ecl/time.hpp>
#include <iostream>
#include <mm_messages.hpp>
#include <sstream>
#include <string>
#include <vector>
#include "mux.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace mm_mux_demux {

/*****************************************************************************
** Interfaces
*****************************************************************************/

typedef mm_messages::Publisher<MessageMux> Publisher;

} // namespace mm_mux_demux

#endif /* mm_mux_demux_PUBLISHER_HPP_ */
