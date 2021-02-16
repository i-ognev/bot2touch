from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.client_pr_callback import client_prsite_call

keyboard_prsite_client = InlineKeyboardMarkup(row_width=2,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton(
                                                          text="🔷 Таргетированная реклама",
                                                          callback_data=client_prsite_call.new(item_name="Таргет_рекл")
                                                      )
                                                  ],
                                                  [
                                                      InlineKeyboardButton(
                                                          text="🔷 Яндекс Директ",
                                                          callback_data=client_prsite_call.new(
                                                              item_name="ЯД")
                                                      ),
                                                      InlineKeyboardButton(
                                                          text="🔶 Google Adwords",
                                                          callback_data=client_prsite_call.new(
                                                              item_name="GA")
                                                      )
                                                  ],
[
                                                      InlineKeyboardButton(
                                                          text="🔷 Весь комплекс",
                                                          callback_data=client_prsite_call.new(
                                                              item_name="Комплекс(продв)")
                                                      ),
                                                      InlineKeyboardButton(
                                                          text="🔶 Другое",
                                                          callback_data=client_prsite_call.new(
                                                              item_name="Другое(продв)")
                                                      )
                                                  ],
[
                                                      InlineKeyboardButton(
                                                          text="🔷 SEO-продвижение",
                                                          callback_data=client_prsite_call.new(item_name="SEO_продв")
                                                      )
                                                  ]

                                              ])