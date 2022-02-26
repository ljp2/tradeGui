from tkinter import *
from tkinter import ttk

import placeorders


class GUI(Tk):
    def buyMKTorder(self):
        quantity = int(self.buy_mkt_quantity.get())
        placeorders.placeBuyMarketOrder(quantity)

    def sellMKTorder(self):
        quantity = int(self.sell_mkt_quantity.get())
        placeorders.placeSellMarketOrder(quantity)

    def buyLMTorder(self):
        quantity = int(self.buy_lim_quantity.get())
        price = float(self.buy_lim_price.get())
        placeorders.placeBuyLimitOrder(quantity, price)

    def sellLMTorder(self):
        quantity = int(self.sell_lim_quantity.get())
        price = float(self.sell_lim_price.get())
        placeorders.placeSellLimitOrder(quantity, price)

        
    def buySTOPorder(self):
        quantity = int(self.buy_stop_quantity.get())
        price = float(self.buy_stop_price.get())
        placeorders.placeBuyStopOrder(quantity, price)


    def sellSTOPorder(self):
        quantity = int(self.sell_stop_quantity.get())
        price = float(self.sell_stop_price.get())
        placeorders.placeSellStopOrder(quantity, price)


    def buyMKTplusBracketOrder(self):
        quantity = int(self.buy_bracket_quantity.get())
        placeorders.placeBuyMKTplusBracketOrder(quantity)

    def sellMKTplusBracketOrder(self):
        quantity = int(self.sell_bracket_quantity.get())
        placeorders.placeSellMKTplusBracketOrder(quantity)


    def __init__(self):
        super().__init__()
        self.title("TWS Trading")

        # MKT Frame
        mktframe = ttk.Labelframe(self, text='MKT orders')
        mktframe.grid(row=0, column=0, padx=10, pady=10)
        mkt_quantity_lbl = ttk.Label(mktframe, text='Quantity')
        mkt_quantity_lbl.grid(row=0, column=1)
        self.buy_mkt_quantity = StringVar(value=100)
        self.sell_mkt_quantity = StringVar(value=100)

        # LONG MKT
        buy_mkt_quantity_btn = ttk.Button(mktframe, text="MKT Buy Order", command=self.buyMKTorder)
        # buy_mkt_quantity_entry = ttk.Entry(mktframe, width=4, textvariable=self.buy_mkt_quantity)
        buy_mkt_quantity_entry = ttk.Spinbox(
            mktframe,
            textvariable=self.buy_mkt_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        buy_mkt_quantity_btn.grid(row=1, column=0, padx=5, pady=5)
        buy_mkt_quantity_entry.grid(row=1, column=1)

        # SHORT MKT
        sell_mkt_quantity_btn = ttk.Button(mktframe, text="MKT Sell Order", command=self.sellMKTorder)
        sell_mkt_quantity_entry = ttk.Spinbox(
            mktframe,
            textvariable=self.sell_mkt_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        sell_mkt_quantity_btn.grid(row=2, column=0, padx=5, pady=5)
        sell_mkt_quantity_entry.grid(row=2, column=1)

        # LMT Frame
        self.buy_lim_price = StringVar(value=0)
        self.buy_lim_quantity = StringVar(value=100)
        self.sell_lim_price = StringVar(value=0)
        self.sell_lim_quantity = StringVar(value=100)

        lmtframe = ttk.Labelframe(self, text='LMT orders')
        lmtframe.grid(row=0, column=1, padx=10, pady=10)
        lmtquantlbl = ttk.Label(lmtframe, text='Quantity')
        lmtpricelbl = ttk.Label(lmtframe, text='Price')
        lmtquantlbl.grid(row=0, column=1)
        lmtpricelbl.grid(row=0, column=2)

        # LONG LMT
        buy_lmt_quantity_btn = ttk.Button(lmtframe, text="LMT Buy Order", command=self.buyLMTorder)
        buy_lmt_quantity_entry = ttk.Spinbox(
            lmtframe,
            textvariable=self.buy_lim_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        buy_lim_price_entry = ttk.Spinbox(
            lmtframe,
            from_= 0,
            to=1000,
            increment=0.5,
            textvariable=self.buy_lim_price,
            width=7
        )
        buy_lmt_quantity_btn.grid(row=1, column=0, padx=5, pady=5)
        buy_lmt_quantity_entry.grid(row=1, column=1)
        buy_lim_price_entry.grid(row=1, column=2)

        # SHORT LMT
        sell_lmt_quantity_btn = ttk.Button(lmtframe, text="LMT Sell Order", command=self.sellLMTorder)
        sell_lmt_quantity_entry = ttk.Spinbox(
            lmtframe,
            textvariable=self.sell_lim_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        sell_lim_price_entry = ttk.Spinbox(
            lmtframe,
            from_= 0,
            to=1000,
            increment=0.5,
            textvariable=self.sell_lim_price,
            width=7
        )
        sell_lmt_quantity_btn.grid(row=2, column=0, padx=5, pady=5)
        sell_lmt_quantity_entry.grid(row=2, column=1, padx=5, pady=5)
        sell_lim_price_entry.grid(row=2, column=2, padx=5, pady=5)





        # STOP Frame
        stopframe = ttk.Labelframe(self, text='STOP orders')
        stopframe.grid(row=0, column=2, padx=10, pady=10)
        stop_quantity_lbl = ttk.Label(stopframe, text='Quantity')
        stop_quantity_lbl.grid(row=0, column=1)
        stop_increment_lbl = ttk.Label(stopframe, text='Increment')
        stop_increment_lbl.grid(row=0, column=2)

        self.buy_stop_price = StringVar(value=0)
        self.buy_stop_quantity = StringVar(value=100)
        self.sell_stop_price = StringVar(value=0)
        self.sell_stop_quantity = StringVar(value=100)
        self.stop_plus_price_increment = StringVar(value=0.5)
        self.stop_minus_price_increment = StringVar(value=0.5)

        # LONG STOP
        buy_stop_quantity_btn = ttk.Button(stopframe, text="STOP Buy Order", command=self.buySTOPorder)
        # buy_stop_quantity_entry = ttk.Entry(stopframe, width=4, textvariable=self.buy_stop_quantity)
        buy_stop_quantity_entry = ttk.Spinbox(
            stopframe,
            textvariable=self.buy_stop_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        stop_plus_entry = ttk.Spinbox(
            stopframe,
            textvariable=self.stop_plus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        buy_stop_quantity_btn.grid(row=1, column=0, padx=5, pady=5)
        buy_stop_quantity_entry.grid(row=1, column=1)
        stop_plus_entry.grid(row=1, column=2)

        # SHORT STOP
        sell_stop_quantity_btn = ttk.Button(stopframe, text="STOP Sell Order", command=self.sellSTOPorder)
        sell_stop_quantity_entry = ttk.Spinbox(
            stopframe,
            textvariable=self.sell_stop_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        stop_minus_entry = ttk.Spinbox(
            stopframe,
            textvariable=self.stop_minus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        sell_stop_quantity_btn.grid(row=2, column=0, padx=5, pady=5)
        sell_stop_quantity_entry.grid(row=2, column=1)
        stop_minus_entry.grid(row=2, column=2)

        # sell_bracket_plus_entry = ttk.Spinbox(
        #     bracframe,
        #     textvariable=self.sell_bracket_plus_price_increment,
        #     from_=0.20,
        #     to=2.00,
        #     increment=0.05,
        #     width=7
        # )
        # sell_bracket_minus_entry = ttk.Spinbox(
        #     bracframe,
        #     textvariable=self.sell_bracket_minus_price_increment,
        #     from_=0.20,
        #     to=2.00,
        #     increment=0.05,
        #     width=7
        # )


        # Bracket Frame
        self.buy_bracket_quantity = StringVar(value=100)
        self.buy_bracket_plus_price_increment = StringVar(value=0.50)
        self.buy_bracket_minus_price_increment = StringVar(value=0.50)
        self.sell_bracket_quantity = StringVar(value=100)
        self.sell_bracket_plus_price_increment = StringVar(value=0.50)
        self.sell_bracket_minus_price_increment = StringVar(value=0.50)

        bracframe = ttk.Labelframe(self, text='Bracket Orders')
        bracframe.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        brac_quantity_lbl = ttk.Label(bracframe, text='Quantity').grid(row=0, column=1)
        brac_plus_lbl = ttk.Label(bracframe, text='Positive Increment').grid(row=0, column=2)
        brac_minus_lbl = ttk.Label(bracframe, text='Negative Increment').grid(row=0, column=3)

        # Buy Bracket
        buy_bracket_btn = ttk.Button(bracframe, text="MKT Buy + Bracket Order", command=self.buyMKTplusBracketOrder)
        buy_bracket_quantity_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.buy_bracket_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        buy_bracket_plus_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.buy_bracket_plus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        buy_bracket_minus_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.buy_bracket_minus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        buy_bracket_btn.grid(row=1, column=0, padx=5, pady=5)
        buy_bracket_quantity_entry.grid(row=1, column=1)
        buy_bracket_plus_entry.grid(row=1, column=2)
        buy_bracket_minus_entry.grid(row=1, column=3)

        # Sell Bracket
        sell_bracket_btn = ttk.Button(bracframe, text="MKT Sell + Bracket Order", command=self.sellMKTplusBracketOrder)
        sell_bracket_quantity_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.sell_bracket_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        sell_bracket_quantity_entry.grid(row=2, column=1)
        sell_bracket_plus_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.sell_bracket_plus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        sell_bracket_minus_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.sell_bracket_minus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        sell_bracket_btn.grid(row=2, column=0, padx=5, pady=5)
        sell_bracket_plus_entry.grid(row=2, column=2)
        sell_bracket_minus_entry.grid(row=2, column=3)


        # Current  Price
        self.current_price = StringVar(value="Current Price")
        current_price_lbl = ttk.Label(self, width=7, padding=10, textvariable=self.current_price )
        current_price_lbl.grid(row = 2, column=0)


        # for child in self.winfo_children():
        #     child.padx = 10
        #     child.pady = 10


if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
