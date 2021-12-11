$(function(){
	console.log('Hello Budget_main page...');

	let date_format = () => {
		let today = new Date;
		let year = today.getFullYear();
		let month = today.getMonth() + 1;
		let date = today.getDate();
		// monthとdateが一桁の際の処理
		if(month < 10){
			month = '0' + month;
		}
		if(date < 10){
			date = '0' + date;
		}
		let formatted = year + '-' + month + '-' + date;

		return formatted
	}

	// ログ入力ボタンをタップした際の処理
	$('#btn_input').on('click', function(){
		console.log('btn_input is clicked');
		let date = date_format();
		$('#input_date').val(date);
		// info_modalを表示
		$('#info_modal').fadeIn(1000, 'swing');
		$('#overlay').fadeIn();
	})

	// modal内のback iconをタップした際の処理
	$('#modal_back_icon').on('click', function(){
		console.log('modal_back_icon is clicked...');
		// info_modalを非表示
		$('#info_modal').fadeOut();
		$('#overlay').fadeOut();
	})

	// modal内のaddボタンをクリックした際の処理
	$('.btn_add').on('click', function(){
		console.log('add button is clicked...')
		// 押されたボタンのidを取得する
		let id = $(this).attr('id');
		console.log('id is ', id);
		// second modalのボタンのneme属性にidを設定する
		$('#btn_insert_item').attr('name', id);
		// second modalを表示
		$('#second_modal').fadeIn(1000, 'swing');
		$('#overlay2').fadeIn();
	})

	// second modalのボタンをクリックした際の処理
	$('#btn_insert_item').on('click', function(){
		console.log('button in second modal is clicked...');
		let id = $(this).attr('name');
		console.log('second modal button name is ', id);
	})

	// second_modal内のback iconをタップした際の処理
	$('#second_modal_back_icon').on('click', function(){
		console.log('second_modal_back_icon is clicked...');
		// info_modalを非表示
		$('#second_modal').fadeOut();
		$('#overlay2').fadeOut();
	})





	// sidebarの開閉処理
	$('#hamburger_icon').on('click', function(){
		console.log('hamburger icon is clicked');
		$('.sidebar').css('display', 'block').animate({left: '0'}, 300);
		$('.sidebar_background').css('display', 'block').animate({opacity: '0.5'}, 300);
	});
	$('.sidebar_back_icon').on('click', function(){
		console.log('sidebar back icon clicked');
		$('.sidebar').animate({left: '-60%'}, 300);
		$('.sidebar_background').animate({opacity: '0'}, 300);
		setTimeout(function(){
			$('.sidebar').css('display', 'none');
			$('.sidebar_background').css('display', 'none');
		}, 300);
	});

	$('#sidebar_main_content_shop_list').on('click', function(){
		console.log('shop list is clicked');
		window.location.href = '/get_shop_lists';
	});

	$('#sidebar_main_content_favorite_shop').on('click', function(){
		window.location.href = '/get_favorite_shops';
	});

	$('#sidebar_main_content_new_shops').on('click', function(){
		window.location.href = '/get_new_shops';
	});

	$('#sidebar_main_content_shop_info').on('click', function(){
		window.location.href = '/get_shop_info';
	});


});