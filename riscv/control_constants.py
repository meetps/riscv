from myhdl import modbv

SRC_A_SEL_WIDTH = 2
SRC_A_RS1  = modbv(0)[SRC_A_SEL_WIDTH:]
SRC_A_PC   = modbv(1)[SRC_A_SEL_WIDTH:]
SRC_A_ZERO = modbv(2)[SRC_A_SEL_WIDTH:]

SRC_B_SEL_WIDTH = 2
SRC_B_RS2  = modbv(0)[SRC_B_SEL_WIDTH:]
SRC_B_IMM  = modbv(1)[SRC_B_SEL_WIDTH:]
SRC_B_FOUR = modbv(2)[SRC_B_SEL_WIDTH:]
SRC_B_ZERO = modbv(3)[SRC_B_SEL_WIDTH:]

PC_SRC_SEL_WIDTH = 3
PC_PLUS_FOUR 	 = modbv(0)[PC_SRC_SEL_WIDTH:]
PC_BRANCH_TARGET = modbv(1)[PC_SRC_SEL_WIDTH:]
PC_JAL_TARGET    = modbv(2)[PC_SRC_SEL_WIDTH:]
PC_JALR_TARGET   = modbv(3)[PC_SRC_SEL_WIDTH:]
PC_REPLAY        = modbv(4)[PC_SRC_SEL_WIDTH:]
PC_HANDLER       = modbv(5)[PC_SRC_SEL_WIDTH:]
PC_EPC           = modbv(6)[PC_SRC_SEL_WIDTH:]

IMM_TYPE_WIDTH = 2
IMM_I = modbv(0)[IMM_TYPE_WIDTH:]
IMM_S = modbv(1)[IMM_TYPE_WIDTH:]
IMM_U = modbv(2)[IMM_TYPE_WIDTH:]
IMM_J = modbv(3)[IMM_TYPE_WIDTH:]

WB_SRC_SEL_WIDTH = 2
WB_SRC_ALU  = modbv(0)[WB_SRC_SEL_WIDTH:]
WB_SRC_MEM  = modbv(1)[WB_SRC_SEL_WIDTH:]
WB_SRC_CSR  = modbv(2)[WB_SRC_SEL_WIDTH:]
WB_SRC_MD   = modbv(3)[WB_SRC_SEL_WIDTH:]

MEM_TYPE_WIDTH = 3
MEM_TYPE_LB   = modbv(0)[MEM_TYPE_WIDTH:]
MEM_TYPE_LH   = modbv(1)[MEM_TYPE_WIDTH:]
MEM_TYPE_LW   = modbv(2)[MEM_TYPE_WIDTH:]
MEM_TYPE_LD   = modbv(3)[MEM_TYPE_WIDTH:]
MEM_TYPE_LBU  = modbv(4)[MEM_TYPE_WIDTH:]
MEM_TYPE_LHU  = modbv(5)[MEM_TYPE_WIDTH:]
MEM_TYPE_LWU  = modbv(6)[MEM_TYPE_WIDTH:]

MEM_TYPE_WIDTH = 3
MEM_TYPE_SB  = modbv(0)[MEM_TYPE_WIDTH:]
MEM_TYPE_SH  = modbv(1)[MEM_TYPE_WIDTH:]
MEM_TYPE_SW  = modbv(2)[MEM_TYPE_WIDTH:]
MEM_TYPE_SD  = modbv(3)[MEM_TYPE_WIDTH:]

HTIF_PCR_WIDTH = 64