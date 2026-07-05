frappe.ui.form.on('Property Owner', {
	refresh(frm) {
		if (frm.doc.supplier) {
			frm.add_custom_button(__('View Supplier'), () => {
				frappe.set_route('Form', 'Supplier', frm.doc.supplier);
			}, __('Links'));
		}
		if (!frm.doc.supplier && !frm.is_new()) {
			frm.add_custom_button(__('Create Supplier'), () => {
				frm.call('_create_supplier').then(() => frm.reload_doc());
			});
		}
	}
});
