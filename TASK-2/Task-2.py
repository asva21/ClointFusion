import ClointFusion as cf

cf.OFF_semi_automatic_mode()

cf.window_show_desktop()
imag_path = r"D:\clointfusion_projects\TASK-2\Images\Snip.png"
imag_coordinates = cf.mouse_search_snip_return_coordinates_x_y(imag_path, conf=0.8)
cf.mouse_click(*imag_coordinates, single_double_triple='double', copyToClipBoard_Yes_No='no')
cf.key_write_enter("Flipkart.com")
cf.key_hit_enter()
cf.key_write_enter("8341616878")
cf.key_press("Tab")
cf.key_write_enter()
imag_coordinates1 = cf.mouse_search_snip_return_coordinates_x_y(r"D:\clointfusion_projects\TASK-2\Images\Search.png",
                                                                conf=0.8)
cf.mouse_click(*imag_coordinates1, single_double_triple='single', copyToClipBoard_Yes_No='no')
cf.key_write_enter("boAt Airdopes 131 Bluetooth Headset")
imag_coordinates2 = cf.mouse_search_snip_return_coordinates_x_y(r"D:\clointfusion_projects\TASK-2\Images\pic1.png",
                                                                conf=0.8)
cf.mouse_click(*imag_coordinates2, single_double_triple='single', copyToClipBoard_Yes_No='no')
imag_coordinates3 = cf.mouse_search_snip_return_coordinates_x_y(r"D:\clointfusion_projects\TASK-2\Images\cart1.png",
                                                                conf=0.8)
cf.mouse_click(*imag_coordinates3, single_double_triple='single', copyToClipBoard_Yes_No='no')
cf.mouse_click(*imag_coordinates1, single_double_triple='single', copyToClipBoard_Yes_No='no')
cf.key_write_enter("boAt Airdopes 402 Bluetooth Headset")
imag_coordinates4 = cf.mouse_search_snip_return_coordinates_x_y(r"D:\clointfusion_projects\TASK-2\Images\pic2.png",
                                                                conf=0.8)
cf.mouse_click(*imag_coordinates4, single_double_triple='single', copyToClipBoard_Yes_No='no')
cf.mouse_click(*imag_coordinates3, single_double_triple='single', copyToClipBoard_Yes_No='no')
imag_coordinates5 = cf.mouse_search_snip_return_coordinates_x_y(
    r"D:\clointfusion_projects\TASK-2\Images\place_order.png", conf=0.8)
cf.mouse_click(*imag_coordinates5, single_double_triple='single', copyToClipBoard_Yes_No='no')
imag_coordinates6 = cf.mouse_search_snip_return_coordinates_x_y(r"D:\clointfusion_projects\TASK-2\Images\deliver.png",
                                                                conf=0.8)
cf.mouse_click(*imag_coordinates6, single_double_triple='single', copyToClipBoard_Yes_No='no')
imag_coordinates7 = cf.mouse_search_snip_return_coordinates_x_y(r"D:\clointfusion_projects\TASK-2\Images\continue.png",
                                                                conf=0.8)
cf.mouse_click(*imag_coordinates7, single_double_triple='single', copyToClipBoard_Yes_No='no')

cf.key_press('Alt + F4')
