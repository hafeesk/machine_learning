// Copyright (c) 2016, hafees and contributors
// For license information, please see license.txt

frappe.ui.form.on('Nodes', {
	refresh: function(frm) {

	},
	create_words: function(frm) {
		frappe.call({
        method: "create_words",
        doc: frm.doc,
        callback: function(r) {
		  		frm.set_value("words",r.message.words)
		  		frm.set_value("lemming_words",r.message.stem_word)
        	}
   		});	
	}
});
