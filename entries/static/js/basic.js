/*
 * SimpleModal Basic Modal Dialog
 * http://simplemodal.com
 *
 * Copyright (c) 2013 Eric Martin - http://ericmmartin.com
 *
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 */

jQuery(function ($) {
	// Load dialog on page load

	// Load dialog on click
	$('#basic-modal').click(function (e) {
		$('#basic-modal-content').modal({ autoResize: true,minHeight:300,minWidth: 300 });

		return false;
	});

	$('#search').click(function (e) {
		$('#search-content').modal({ autoResize: true,minHeight:300,minWidth: 300 });
		return false;
	});
});