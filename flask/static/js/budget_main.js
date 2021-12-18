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

	// DBのマスターテーブルの値を格納する処理
	let master_datas = {};

	// ログ入力ボタンをタップした際の処理
	$('#btn_input').on('click', function(){
		console.log('btn_input is clicked');

		// DBのマスターデータを全件取得する処理
		$.ajax({
			type: 'GET',
	        url: 'http://localhost:5000/select_items', 
	        contentType: 'application/json',
	        dataType: 'json'
		}).then(function(response){
			console.log('DB master datas: ' + response);
			console.log(response);
			master_datas = response;
			console.log(response['Budget_classification']);
			console.log(response['Budget_classification'][0]);
			console.log(response['Budget_classification'][0]['class_id']);
			console.log(master_datas['Budget_classification'][0]);
			console.log(master_datas['Budget_classification'][0]['class_id']);

			// 各selectタグへ値の入れ込み
			// Categoryのselect
			for(let i=0; i<master_datas['Budget_category'].length; i++){
				if(master_datas['Budget_category'][i]['category_id'] == 2){
					// outgoをselectedにする
					$('#select_category').append('<option value="' + master_datas['Budget_category'][i]['category_id'] + '" selected>' + master_datas['Budget_category'][i]['category_name'] + '</option>');
				}
				else{
					$('#select_category').append('<option value="' + master_datas['Budget_category'][i]['category_id'] + '">' + master_datas['Budget_category'][i]['category_name'] + '</option>');
				}
			}

			// Classificationのselect
			for(let i=0; i<master_datas['Budget_classification'].length; i++){
				if(master_datas['Budget_classification'][i]['class_id'] == 2){
					// variable costをselectedにする
					$('#select_classification').append('<option value="' + master_datas['Budget_classification'][i]['class_id'] + '" selected>' + master_datas['Budget_classification'][i]['class_name'] + '</option>');
				}
				else{
					$('#select_classification').append('<option value="' + master_datas['Budget_classification'][i]['class_id'] + '">' + master_datas['Budget_classification'][i]['class_name'] + '</option>');
				}
			}

			// Todo DBにデータを格納次第、Section, Kind, Groupのselectを追加する

			let date = date_format();
			$('#input_date').val(date);
			// info_modalを表示
			$('#info_modal').fadeIn(1000, 'swing');
			$('#overlay').fadeIn();
			
		}, function(error){
			console.log('DB master datas error: ' + error);
		});
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

		// 入力するマスタの親マスタの表示の可否を判定する処理
		switch(id){
			case 'section':
				console.log('switch: section is called...');
				// selectタグへ値の入れ込み
				for(let i=0; i<master_datas['Budget_classification'].length; i++){
					if(master_datas['Budget_classification'][i]['class_id'] == 2){
						// variable costをselectedにする
						$('#modal_select_parent').append('<option value="' + master_datas['Budget_classification'][i]['class_id'] + '" selected>' + master_datas['Budget_classification'][i]['class_name'] + '</option>');
					}
					else{
						$('#modal_select_parent').append('<option value="' + master_datas['Budget_classification'][i]['class_id'] + '">' + master_datas['Budget_classification'][i]['class_name'] + '</option>');
					}
				}
				$('.parent').show();
				break;
			case 'group':
				console.log('switch: group is called...');
				// Todo DBにデータを格納次第、Groupのselectを追加する
				$('.parent').show();
				break;
			case 'kind':
				console.log('switch: kind is called...');
				break;
			default:
				console.log('Error: something occured...');
				alert('Cannot register the item.Please do again.')
		}

		// second modalを表示
		$('#second_modal').fadeIn(1000, 'swing');
		$('#overlay2').fadeIn();
	})

	// second modalのボタンをクリックした際の処理
	$('#btn_insert_item').on('click', function(){
		console.log('button in second modal is clicked...');
		// 押されたボタンのidを取得する
		let id = $(this).attr('name');
		// 入力データを取得する
		let inputted_data = $('#master_data').val();
		// selectタグのデータを取得する
		let selected_data = $('#modal_select_parent').val();
		console.log('second modal button name is ', id);
		console.log('inputted data: ', inputted_data);
		console.log('selected data: ', selected_data);

		send_datas = {
			'table_name': id,
			'inputted_data': inputted_data,
			'selected_data': selected_data
		}

		// 入力データをサーバーへPOST
		$.ajax({
			type: 'POST',
	        contentType: 'application/json',
	        url: 'http://localhost:5000/budget_main', 
	        data: JSON.stringify(send_datas),
	        dataType: 'json'
		}).then(function(response){
			console.log('btn_insert_item response: ' + response);
		}, function(error){
			console.log('btn_insert_item error: ' + error);
		});
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