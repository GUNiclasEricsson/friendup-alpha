import flet as ft
 
# Use of GestureDetector for with on_pan_update event for dragging card
# Absolute positioning of controls within stack
 
def main(page: ft.Page):
 
   def drag(e: ft.DragUpdateEvent):
       e.control.top = max(0, e.control.top + e.delta_y)
       #e.control.left = max(0, e.control.left + e.delta_x)
       e.control.bottom = min(0, e.control.bottom - e.delta_y)
       e.control.update()
 
   card = ft.GestureDetector(
       mouse_cursor=ft.MouseCursor.MOVE,
       drag_interval=1,
       on_pan_update=drag,
       #left=0,
       bottom=0,
       top=0,
       content=ft.Container(bgcolor=ft.colors.GREEN, width=400, height=700),
   )   
 
   page.add(ft.Stack(controls=[card], width=400, height=700))
 
ft.app(target=main)