"""
Dimensions quick launcher menubar for OSx
"""

from menus import *

import rumps
rumps.debug_mode(True)
from rumps import *
import webbrowser
from collections import OrderedDict



def generic_menu_builder(title, MENU_DICT):
	"Reusable code to build menus from a dict"
	menu = rumps.MenuItem(title)
	MESSAGE = """Tip: Right-click inside the text area to "Paste" text."""
	for title, value in MENU_DICT.items():
		def cb(sender):
			# print(sender.value)
			window = rumps.Window(message=MESSAGE, title=f'{title}: {sender.title}', default_text='', ok="Go!", cancel=True)
			window.icon = "dimensions.icns"
			response = window.run()
			if response.clicked:
				url = sender.value.format(response.text)
				webbrowser.open(url)
			else:
				pass
		mi = rumps.MenuItem(title, callback=cb)
		mi.value = value
		menu[title] = mi

	return menu


class DimensionsApp(rumps.App):

	def __init__(self):

		menu_spec = [
			"Open Dimensions",
			"Full text search",
			None,
			('Identifiers', [self._build_pubs_submenu(), 
							self._build_grants_submenu(),
							self._build_patent_submenu(),
							self._build_poldoc_submenu(),
							self._build_cltrial_submenu(),
							self._build_dataset_submenu(),
							self._build_res_submenu(),
							self._build_orgs_submenu(),
							]),
			None,
			# self._build_categories_submenu(),
			# None,
		]

		super(DimensionsApp, self).__init__("Dimensions", menu=menu_spec)

		# TIP mac icons: copy image, open in Preview, save as .icns
		self.icon = "dimensions.icns"

	@rumps.clicked("Open Dimensions")
	def open_dimensions(self, _):
		webbrowser.open("https://app.dimensions.ai/")

	@rumps.clicked("Full text search")
	def search(self, _):

		window = rumps.Window(message='Enter some text', title='Full text search - Dimensions', default_text='', ok="Go!", cancel=True)
		window.icon = self.icon
		response = window.run()
		# print(response)
		if response.clicked:
			url = f"https://app.dimensions.ai/discover/publication?search_mode=content&search_text={response.text}&search_type=kws&search_field=full_search"
			webbrowser.open(url)
		else:
			pass


	def _build_pubs_submenu(self):
		return generic_menu_builder("Publication", PUBS_MENU)

	def _build_grants_submenu(self):
		return generic_menu_builder("Grant", GRANTS_MENU)

	def _build_patent_submenu(self):
		return generic_menu_builder("Patent", PATENTS_MENU)

	def _build_poldoc_submenu(self):
		return generic_menu_builder("Policy Document", POLICY_DOCUMENTS_MENU)

	def _build_cltrial_submenu(self):
		return generic_menu_builder("Clinical Trial", CLINICAL_TRIALS_MENU)

	def _build_dataset_submenu(self):
		return generic_menu_builder("Dataset", DATASETS_MENU)

	def _build_res_submenu(self):
		return generic_menu_builder("Researcher", RESEARCHERS_MENU)

	def _build_orgs_submenu(self):
		return generic_menu_builder("Organization", GRID_MENU)

	def _build_categories_submenu(self):
		menu = rumps.MenuItem("Categories")
		for title, value in CATEGORIES_MENU.items():
			def cb(sender):
				print(sender)
			mi = rumps.MenuItem(title, callback=cb)
			mi.value = value
			menu[title] = mi

		return menu

if __name__ == "__main__":
	DimensionsApp().run()