$(document).ready(function(){
			$('#qr_scan').click(function(){
				$('#waste_bin_status').html("Scanning..");
				$('#reader').html5_qrcode(function(data){
				 		 // do something when code is read
				 		 alert('Scan successful!');
				 		 $.post( 
				 		 		"/ajax",
				 		 		{ 
				 		 			code: data,
				 		 			csrfmiddlewaretoken:'{{ csrf_token }}'
				 		 		 },
				 		 		function(mqtt_response,status){
				 		 			$("#reader").html5_qrcode_stop();
				 		 			$("#server_response").html(mqtt_response);
				 		 			if(mqtt_response === "true")
				 		 				$('#waste_bin_status').html("Open");
				 		 		});

				 		 
				 		 $('#waste_bin_status').html("Scan complete!");
				 		 return;
				 	},
				 	function(error){
						//show read errors 
						console.log(error);
						/*$("#reader").html5_qrcode_stop();*/
						$('#waste_bin_status').html("Scan Error!!!");
					}, function(videoError){
						//the video stream could be opened
						console.log(videoError);
						$("#reader").html5_qrcode_stop();
						$('#waste_bin_status').html("Video Error!!");
					}
				);
			});
		});