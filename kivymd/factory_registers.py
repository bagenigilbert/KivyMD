"""
Register KivyMD widgets to use without import
"""

from kivy.factory import Factory

r = Factory.register
r("MDAccordion", module="kivymd.uix.accordion")
r("MDAccordionItem", module="kivymd.uix.accordion")
r("MDAccordionSubItem", module="kivymd.uix.accordion")
r("MDAccordionItemTitleLayout", module="kivymd.uix.accordion")
r("MDAccordionListItem", module="kivymd.uix.accordionlistitem")
r("AccordionListItem", module="kivymd.uix.accordionlistitem")
r("MDTab", module="kivymd.uix.bottomnavigation")
r("MDBottomNavigation", module="kivymd.uix.bottomnavigation")
r("MDBottomNavigationItem", module="kivymd.uix.bottomnavigation")
r("MDBottomNavigationHeader", module="kivymd.uix.bottomnavigation")
r("MDBottomNavigationBar", module="kivymd.uix.bottomnavigation")
r("MDBottomSheet", module="kivymd.uix.bottomsheet")
r("MDListBottomSheet", module="kivymd.uix.bottomsheet")
r("MDGridBottomSheet", module="kivymd.uix.bottomsheet")
r("MDIconButton", module="kivymd.uix.button")
r("MDFlatButton", module="kivymd.uix.button")
r("MDRaisedButton", module="kivymd.uix.button")
r("MDFloatingActionButton", module="kivymd.uix.button")
r("MDRectangleFlatButton", module="kivymd.uix.button")
r("MDTextButton", module="kivymd.uix.button")
r("MDCustomRoundIconButton", module="kivymd.uix.button")
r("MDFillRoundFlatButton", module="kivymd.uix.button")
r("MDRectangleFlatIconButton", module="kivymd.uix.button")
r("MDRoundFlatIconButton", module="kivymd.uix.button")
r("MDFillRoundFlatIconButton", module="kivymd.uix.button")
r("MDCard", module="kivymd.uix.card")
r("MDSeparator", module="kivymd.uix.card")
r("MDCardPost", module="kivymd.uix.card")
r("MDChip", module="kivymd.uix.chip")
r("MDChooseChip", module="kivymd.uix.chip")
r("MDDialog", module="kivymd.uix.dialog")
r("MDInputDialog", module="kivymd.uix.dialog")
r("MDFanScreenManager", module="kivymd.uix.fanscreenmanager")
r("MDFanScreen", module="kivymd.uix.fanscreenmanager")
r("MDFileManager", module="kivymd.uix.filemanager")
r("Tile", module="kivymd.uix.imagelist")
r("SmartTile", module="kivymd.uix.imagelist")
r("SmartTileWithLabel", module="kivymd.uix.imagelist")
r("SmartTileWithStar", module="kivymd.uix.imagelist")
r("MDLabel", module="kivymd.uix.label")
r("MDIcon", module="kivymd.uix.label")
r("MDList", module="kivymd.uix.list")
r("ILeftBody", module="kivymd.uix.list")
r("ILeftBodyTouch", module="kivymd.uix.list")
r("IRightBody", module="kivymd.uix.list")
r("IRightBodyTouch", module="kivymd.uix.list")
r("ContainerSupport", module="kivymd.uix.list")
r("OneLineListItem", module="kivymd.uix.list")
r("TwoLineListItem", module="kivymd.uix.list")
r("ThreeLineListItem", module="kivymd.uix.list")
r("OneLineAvatarListItem", module="kivymd.uix.list")
r("TwoLineAvatarListItem", module="kivymd.uix.list")
r("ThreeLineAvatarListItem", module="kivymd.uix.list")
r("OneLineIconListItem", module="kivymd.uix.list")
r("TwoLineIconListItem", module="kivymd.uix.list")
r("ThreeLineIconListItem", module="kivymd.uix.list")
r("OneLineRightIconListItem", module="kivymd.uix.list")
r("TwoLineRightIconListItem", module="kivymd.uix.list")
r("ThreeLineRightIconListItem", module="kivymd.uix.list")
r("OneLineAvatarIconListItem", module="kivymd.uix.list")
r("TwoLineAvatarIconListItem", module="kivymd.uix.list")
r("ThreeLineAvatarIconListItem", module="kivymd.uix.list")
r("ThreeLineAvatarIconListItem", module="kivymd.uix.managerswiper")
r("MDSwiperManager", module="kivymd.uix.managerswiper")
r("MDSwiperPagination", module="kivymd.uix.managerswiper")
r("ItemPagination", module="kivymd.uix.managerswiper")
r("MDMenu", module="kivymd.uix.menu")
r("MDDropdownMenu", module="kivymd.uix.menu")
r("MDMenuItem", module="kivymd.uix.menu")
r("MDNavigationDrawer", module="kivymd.uix.navigationdrawer")
r("NavigationLayout", module="kivymd.uix.navigationdrawer")
r("NavigationDrawerHeaderBase", module="kivymd.uix.navigationdrawer")
r("NavigationDrawerToolbar", module="kivymd.uix.navigationdrawer")
r("NavigationDrawerIconButton", module="kivymd.uix.navigationdrawer")
r("NavigationDrawerSubheader", module="kivymd.uix.navigationdrawer")
r("NavigationDrawerDivider", module="kivymd.uix.navigationdrawer")
r("NDIconLabel", module="kivymd.uix.navigationdrawer")
r("NDBadgeLabel", module="kivymd.uix.navigationdrawer")
r("MDDatePicker", module="kivymd.uix.picker")
r("MDTimePicker", module="kivymd.uix.picker")
r("MDThemePicker", module="kivymd.uix.picker")
r("MDPopupScreen", module="kivymd.uix.popupscreen")
r("MDProgressBar", module="kivymd.uix.progressbar")
r("MDProgressLoader", module="kivymd.uix.progressloader")
r("MDScrollViewRefreshLayout", module="kivymd.uix.refreshlayout")
r("MDCheckbox", module="kivymd.uix.selectioncontrol")
r("MDSwitch", module="kivymd.uix.selectioncontrol")
r("MDSlider", module="kivymd.uix.slider")
r("SlidingPanel", module="kivymd.uix.slidingpanel")
r("Snackbar", module="kivymd.uix.snackbar")
r("MDSpinner", module="kivymd.uix.spinner")
r("MDStackFloatingButtons", module="kivymd.uix.stackfloatingbutton")
r("MDFloatingLabel", module="kivymd.uix.stackfloatingbutton")
r("MDFloatingLabel", module="kivymd.uix.tab")
r("MDTabsLabel", module="kivymd.uix.tab")
r("MDTabsBase", module="kivymd.uix.tab")
r("MDTabsMain", module="kivymd.uix.tab")
r("MDTabsCarousel", module="kivymd.uix.tab")
r("MDTabsScrollView", module="kivymd.uix.tab")
r("MDTabsBar", module="kivymd.uix.tab")
r("MDTabs", module="kivymd.uix.tab")
r("MDTextField", module="kivymd.uix.textfield")
r("MDTextField", module="kivymd.uix.textfield")
r("MDTextFieldRound", module="kivymd.uix.textfield")
r("MDTextFieldRect", module="kivymd.uix.textfield")
r("MDTextFieldClear", module="kivymd.uix.textfield")
r("MDToolbar", module="kivymd.uix.toolbar")
r("MDBottomAppBar", module="kivymd.uix.toolbar")
r("MDUserAnimationCard", module="kivymd.uix.useranimationcard")
r("MDDropDownItem", module="kivymd.uix.dropdownitem")
