from django.core.exceptions import ValidationError
from lists.models import Item, List
from django.test import TestCase

class ListAndItemModelsTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list_l = List()
		list_l.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.listt = list_l
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.listt = list_l
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_l)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]

		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.listt, list_l)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.listt, list_l)


	def test_cannot_save_empty_list_items(self):
		list_ = List.objects.create()
		item = Item(listt=list_, text = '')
		with self.assertRaises(ValidationError):
			item.save()
			item.full_clean()

	def test_get_absolute_url(self):
		list_l = List.objects.create()
		self.assertEqual(list_l.get_absolute_url(), f'/lists/{list_l.id}/')