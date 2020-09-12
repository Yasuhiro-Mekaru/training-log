$(function(){
	console.log('index.html: jquery Start');

	$('#button_bicycle').click(function(){
		window.location.href = 'https://training-logs.herokuapp.com/bicycle_contents'
	})
});
