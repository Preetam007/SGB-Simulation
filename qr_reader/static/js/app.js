(function (dragula, global) {
	"use strict";

	var wasteTypesContainer = document.getElementById('wastes');
	var trashContainer = document.getElementById('trash');
	var dashboardContainer = document.getElementById('info').getElementsByClassName('content-body')[0];

	var container = [wasteTypesContainer, trashContainer];

	var dragger = dragula(container, {
		accepts: function (el, target) {
			return target !== wasteTypesContainer;
		},
		copy: function (el, source) {
		    return source === wasteTypesContainer;
		},
		revertOnSpill: true
	});

	dragger.on('drop', function(el) {
		el.classList.add('hidden');
		if ( dashboardContainer.innerHTML.indexOf('Closed') !== -1 ) {
			dashboardContainer.innerHTML = " ";
		}
		dashboardContainer.innerHTML += '<p> ' + el.getAttribute('data-type') + " collected. </p>";
		dashboardContainer.scrollTop = dashboardContainer.scrollHeight;
		console.log('Dropped');
	});

	dragger.on('out', function() {
		trashContainer.classList.remove('trash--open');
		console.log('Out of container');
	});

	dragger.on('over', function() {
		trashContainer.classList.add('trash--open');
		console.log('Came to container');
	});

}(dragula, window));