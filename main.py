from PIL import Image, ExifTags
import exif
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from rich import print as print	
import sys
import rich
from time import sleep
from rich.progress import track
import random	
import warnings
import os

try:
	warnings.filterwarnings("ignore", category=RuntimeWarning) 
	console = Console()
	os.system("cls")

	all_all_exif = ['_exif_ifd_pointer', '_gps_ifd_pointer', 'aperture_value', 'brightness_value', 'color_space',
	 'components_configuration', 'compression', 'datetime', 'datetime_digitized', 'datetime_original', 'exif_version',
	 'exposure_bias_value', 'exposure_mode', 'exposure_program', 'exposure_time', 'f_number', 'flash',
	 'flashpix_version', 'focal_length', 'focal_length_in_35mm_film', 'gps_altitude', 'gps_altitude_ref',
	 'gps_datestamp', 'gps_dest_bearing', 'gps_dest_bearing_ref', 'gps_horizontal_positioning_error',
	 'gps_img_direction', 'gps_img_direction_ref', 'gps_latitude', 'gps_latitude_ref', 'gps_longitude',
	 'gps_longitude_ref', 'gps_speed', 'gps_speed_ref', 'gps_timestamp', 'jpeg_interchange_format',
	 'jpeg_interchange_format_length', 'lens_make', 'lens_model', 'lens_specification', 'make', 'maker_note',
	 'metering_mode', 'model', 'orientation', 'photographic_sensitivity', 'pixel_x_dimension', 'pixel_y_dimension',
	 'resolution_unit', 'scene_capture_type', 'scene_type', 'sensing_method', 'shutter_speed_value', 'software',
	 'subject_area', 'subsec_time_digitized', 'subsec_time_original', 'white_balance', 'x_resolution',
	 'y_and_c_positioning', 'y_resolution']
	logo = """
            /$$                                         /$$ /$$                          
           |__/                                        |__/| $$                          
 /$$    /$$ /$$  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$| $$$$$$$  /$$   /$$  /$$$$$$$
|  $$  /$$/| $$ /$$_____/ /$$_____/ /$$__  $$ /$$__  $$| $$| $$__  $$| $$  | $$ /$$_____/
 \\  $$/$$/ | $$|  $$$$$$ | $$      | $$$$$$$$| $$  \\__/| $$| $$  \\ $$| $$  | $$|  $$$$$$ 
  \\  $$$/  | $$ \\____  $$| $$      | $$_____/| $$      | $$| $$  | $$| $$  | $$ \____  $$
   \\  $/   | $$ /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$      | $$| $$$$$$$/|  $$$$$$/ /$$$$$$$/
    \\_/    |__/|_______/  \\_______/ \\_______/|__/      |__/|_______/  \\_____/ |_______/
	"""
	print(Align(Panel(logo, style="#950000", title="EXIF editor utulite"), align='center'))
	sleep(0.7)
	print(Align("by 0x7b", style="#950000", align='center'))
	sleep(0.5)
	print(Align("THE361 - @the361soft", style="#950000", align='center'))
	for i in track(range(100), description="Loading..."):
		sleep(0.005)

	while True:
		print(Align("Select mode:\n1 - read\n2 - edit\n3 - remove\n Press enter to exit", style="Bold #950000"))
		mode = input("->")
		if mode == "1": #read

			print(Align("Enter the path to the file for which you want to read EXIF data", style="Bold #950000"))
			name = input("->")
			try:
				with open(name, 'rb') as file:
					file = exif.Image(file)
				if file.has_exif != False:
					print(Align("Succes! EXIF data finded!", style="green"))
					file_exif_data = file.list_all()
					for i in file_exif_data:
						print(f"{str(i)}: " + str(file[i]))	
					

				else:
					print("Erorr: File dont have a EXIF data")
			except:
				print(Align("Erorr\nFile not find or other erorr", style="bold red"))



		elif mode == "2": #edit
			print("")
			
			print(Align("Enter the path to the file for which you want to edit EXIF data", style="Bold #950000"))
			name = input("->")
			try:
				with open(name, 'rb') as file:
					file = exif.Image(file)
					if file.has_exif != False:
						print(Align("Succes! EXIF data finded!", style="green"))
						file_exif_data = file.list_all()
						for i in file_exif_data:
							print(f"{str(i)}: " + str(file[i]))	
						print(Align("Enter a EXIF property:", style="bold yellow"))
						exif_edit = input("->")
						for i in file_exif_data:		
							if str(i)== exif_edit:
								print(Align("Enter a meaning for u property:", style="bold yellow"))
								meaning = input("->")
								file[exif_edit] = str(meaning)	
								with open(f'edited{name}', 'wb') as new:
									new.write(file.get_file())
								print(Align(f"Property {exif_edit} successfully modified to {meaning}", style="bold green"))
			


			

					else:
						print("Erorr: File dont have a EXIF data")
			except:
					print(Align("Erorr\nFile not find or other erorr", style="bold red"))

		elif mode == "3": #remove
			print(Align("Enter the path to the file for which you want to remove EXIF data", style="Bold #950000"))
			name = input("->")
			try:
				with open(name, 'rb') as file:
					file = exif.Image(file)
					if file.has_exif != False:
						print(Align("Succes! EXIF data finded!", style="green"))
						file_exif_data = file.list_all()
						for i in file_exif_data:
							print(f"{str(i)}: " + str(file[i]))	
					print(Align("Select mode:\n1 - remove all exif\n 2 - remove select EXIF(In development)", style="bold yellow"))
					mode = input("->")
					if mode == "1":
						print(Align("Warning!\nDeleting some properties may not work due to an error!", style="bold red"))
						file.delete_all()
						with open(f'new{name}', 'wb') as new:
							new.write(file.get_file())
					elif mode == "2":
						print(Align("Enter a propety for delete:"))
						exif_edit = input("->")
						for i in file_exif_data:
							if str(i) == exif_edit:
								file.delete(f'{i}')
			except:
				print(Align("Erorr\nFile not find or other erorr", style="bold red"))



					

		elif mode == "":
			print("Exit..")
			sys.exit()
		elif mode == "361":
			for i in track(range(99999), description="Loading..."):
				sleep(0.001)
			print("You found an Easter egg")
		else:
			print("Invalid mode!")
except:
	print("Fatal erorr!")



