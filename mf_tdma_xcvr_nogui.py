#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SC2 Bot MF-TDMA Transciever
# Author: Michael Wentz <michael.wentz@ll.mit.edu>
# Generated: Fri Apr 14 11:21:13 2017
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import spectrum_challenge
import time


class mf_tdma_xcvr_nogui(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "SC2 Bot MF-TDMA Transciever")

        ##################################################
        # Variables
        ##################################################
        self.config_file = config_file = None
        self.samp_rate = samp_rate = 2e6
        self.cfh = cfh = spectrum_challenge.Config_File_Helper(config_file)

        ##################################################
        # Blocks
        ##################################################

        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_0.set_subdev_spec('A:0', 0)
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(cfh.fc, 20e6), 0)
        self.uhd_usrp_source_0_0.set_gain(cfh.rx_gain, 0)
        self.uhd_usrp_source_0_0.set_antenna('RX2', 0)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        	"tx_pkt_len",
        )
        self.uhd_usrp_sink_0_0.set_subdev_spec('A:0', 0)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(uhd.tune_request(cfh.fc, 20e6), 0)
        self.uhd_usrp_sink_0_0.set_gain(cfh.tx_gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        (self.uhd_usrp_sink_0_0).set_block_alias("tx_usrp")
        self.spectrum_challenge_mf_tdma_tx_mc_0_0 = spectrum_challenge.mf_tdma_tx_mc(cfh.bot_id, cfh.num_nodes, False, ['192.168.20.0', '192.168.20.1', '192.168.20.2', '192.168.20.3', '192.168.20.4'] , cfh.init_assign, 0.4, "usrp-pc", samp_rate, 2, 0.33, 'tx_usrp')
        self.spectrum_challenge_mf_tdma_rx_cm_0_0 = spectrum_challenge.mf_tdma_rx_cm(cfh.bot_id, len(cfh.init_assign), samp_rate, 50e-9, 5000, 2, 0.33, 0, 6)
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_vcc((0.7, ))
        (self.blocks_multiply_const_vxx_1_0_0).set_min_output_buffer(1000000)
        self.blocks_message_debug_0_0 = blocks.message_debug()


        ##################################################
        # User Edits Start Here
        ##################################################

        # Depending on the SRN you may want different destinations.  For the time being,
        # you'll have to add and subtract different GR blocks for each destination.
        # This flowgraph is setup to send packets to every other node in the network.                                                        +--- Destination IP
        #                                                                                                                                    |
        #                                                                                                                                    |
        if cfh.bot_id != 0:  #                                                                                                               v
            self.spectrum_challenge_udp_ip_debug_src_m_0 = spectrum_challenge.udp_ip_debug_src_m(123, '192.168.20.' + str(cfh.bot_id), 234, '192.168.20.0', 1000, 100, 4, 0)
            self.msg_connect((self.spectrum_challenge_udp_ip_debug_src_m_0, 'out'), (self.spectrum_challenge_mf_tdma_tx_mc_0_0, 'in'))

        if cfh.bot_id != 1:
            self.spectrum_challenge_udp_ip_debug_src_m_1 = spectrum_challenge.udp_ip_debug_src_m(123, '192.168.20.' + str(cfh.bot_id), 234, '192.168.20.1', 1000, 100, 4, 0)
            self.msg_connect((self.spectrum_challenge_udp_ip_debug_src_m_1, 'out'), (self.spectrum_challenge_mf_tdma_tx_mc_0_0, 'in'))

        if cfh.bot_id != 2:
            self.spectrum_challenge_udp_ip_debug_src_m_2 = spectrum_challenge.udp_ip_debug_src_m(123, '192.168.20.' + str(cfh.bot_id), 234, '192.168.20.2', 1000, 100, 4, 0)
            self.msg_connect((self.spectrum_challenge_udp_ip_debug_src_m_2, 'out'), (self.spectrum_challenge_mf_tdma_tx_mc_0_0, 'in'))

        if cfh.bot_id != 3:
            self.spectrum_challenge_udp_ip_debug_src_m_3 = spectrum_challenge.udp_ip_debug_src_m(123, '192.168.20.' + str(cfh.bot_id), 234, '192.168.20.3', 1000, 100, 4, 0)
            self.msg_connect((self.spectrum_challenge_udp_ip_debug_src_m_3, 'out'), (self.spectrum_challenge_mf_tdma_tx_mc_0_0, 'in'))

        if cfh.bot_id != 4:
            self.spectrum_challenge_udp_ip_debug_src_m_4 = spectrum_challenge.udp_ip_debug_src_m(123, '192.168.20.' + str(cfh.bot_id), 234, '192.168.20.4', 1000, 100, 4, 0)
            self.msg_connect((self.spectrum_challenge_udp_ip_debug_src_m_4, 'out'), (self.spectrum_challenge_mf_tdma_tx_mc_0_0, 'in'))


        ##################################################
        # User Edit End Here
        ##################################################

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.spectrum_challenge_mf_tdma_rx_cm_0_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.spectrum_challenge_mf_tdma_tx_mc_0_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.spectrum_challenge_mf_tdma_rx_cm_0_0, 0))

    def get_config_file(self):
        return self.config_file

    def set_config_file(self, config_file):
        self.config_file = config_file
        self.set_cfh(spectrum_challenge.Config_File_Helper(self.config_file))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)

    def get_cfh(self):
        return self.cfh

    def set_cfh(self, cfh):
        self.cfh = cfh


def main(top_block_cls=mf_tdma_xcvr_nogui, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
