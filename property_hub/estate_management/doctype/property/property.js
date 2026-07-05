frappe.ui.form.on('Property', {
	refresh(frm) {
		frm.add_custom_button(__('Units'), () => {
			frappe.set_route('List', 'Property Unit', { property: frm.doc.name });
		}, __('View'));
		frm.add_custom_button(__('Lease Contracts'), () => {
			frappe.set_route('List', 'Lease Contract', { property: frm.doc.name });
		}, __('View'));
		frm.add_custom_button(__('Maintenance Requests'), () => {
			frappe.set_route('List', 'Maintenance Request', { property: frm.doc.name });
		}, __('View'));
	}
});
