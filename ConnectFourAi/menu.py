
import consts
import pygame
import time
import os


pygame.init()
clock = pygame.time.Clock()

class MainMenu():

    def __int__(self):

        self.win = pygame.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))

        self.finish = False
        self.in_menu = True
        self.in_settings = False
        self.in_guide = False
        self.BattleMode = [["Player Vs Player" , "Player Vs AiBot" , "Player Vs RandomBot"] , ["AiBot Vs Player", "AiBot Vs AiBot", "AiBot Vs RandomBot"], ["RandomBot Vs Player", "RandomBot Vs AiBot", "RandomBot Vs RandomBot"]]
        self.ModeLevel1 = 0
        self.ModeLevel2 = 1

        self.AllColors = [consts.RED, consts.YELLOW, consts.DARK_BLUE, consts.LEAF_GREEN, consts.PURPLE,consts.PINK]
        self.AllColorsNames = ["Red", "Yellow", "Blue", "Green", "Purple","Pink"]
        self.DiscColor1 = 0
        self.DiscColor2 = 1

        self.settings_page = 1
        self.DepthBot1 = 5
        self.DepthBot2 = 5
        self.Funny = False  # funny function on/off


    def is_click_on_rect(self, rect):
        x, y = pygame.mouse.get_pos()

        if x > rect[0] and x < rect[0] + rect[2]:
            if y > rect[1] and y < rect[1] + rect[3]:
                #print(x, y)
                return True
        return False

    def text_objects(self,text, font, text_color):
        textSurface = font.render(text, True, text_color)
        return textSurface, textSurface.get_rect()

    def create_text(self,text_str, x, y, text_size, text_color=consts.BLACK, center=True):
        text_font = pygame.font.Font('freesansbold.ttf', int(text_size))
        text, text_rect = self.text_objects(text_str, text_font, text_color)
        if center:
            text_rect.center = (x, y)
        else:
            text_rect = pygame.rect.Rect(x, y, 0, 0)
        return text, text_rect


    def remove_img_background(self, img, color_key=consts.WHITE):
        if img.get_alpha():
            img = img.convert_alpha()
        else:
            img = img.convert()
            img.set_colorkey(color_key)
        return img


    def rot_center(self, image, angle, x, y, RemoveBackground=True):
        if (RemoveBackground):
            image = self.remove_img_background(image)
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
        return rotated_image, new_rect


    def game_guide(self):
        self.GuideTitleText = self.create_text("Guide", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT*0.1,consts.WIN_WIDTH / 8, consts.GOLD)

        self.guide_texts = []
        txt_color = consts.GRAY
        self.guide_texts.append(self.create_text("Game Guide:", consts.WIN_WIDTH / 100, consts.WIN_HEIGHT * 0.19,consts.WIN_WIDTH * 0.07, consts.LIGHT_GREEN , center=False))
        self.guide_texts.append(self.create_text("Mouse / Arrow keys to move columns", consts.WIN_WIDTH / 100, consts.WIN_HEIGHT * 0.28, consts.WIN_WIDTH * 0.05,txt_color , center=False))
        self.guide_texts.append(self.create_text("Right click / Up arrow key to start a game", consts.WIN_WIDTH / 100,consts.WIN_HEIGHT * 0.36, consts.WIN_WIDTH * 0.0495, txt_color, center=False))
        self.guide_texts.append(self.create_text("Left click / Up arrow key to place piece", consts.WIN_WIDTH / 100,consts.WIN_HEIGHT * 0.44, consts.WIN_WIDTH  * 0.05, txt_color, center=False))

        self.guide_texts.append(self.create_text("Settings Guide:", consts.WIN_WIDTH / 100, consts.WIN_HEIGHT * 0.53, consts.WIN_WIDTH * 0.07,consts.LIGHT_GREEN, center=False))
        self.guide_texts.append(self.create_text("Left/Right click to change Battle Mod", consts.WIN_WIDTH / 100,consts.WIN_HEIGHT * 0.62, consts.WIN_WIDTH * 0.05, txt_color, center=False))
        self.guide_texts.append(self.create_text("Left/Right click to change piece colors", consts.WIN_WIDTH / 100,consts.WIN_HEIGHT * 0.68, consts.WIN_WIDTH * 0.05, txt_color, center=False))
        self.guide_texts.append(self.create_text("*only at BattleModes right click doesn't go back", consts.WIN_WIDTH / 100,consts.WIN_HEIGHT * 0.745, consts.WIN_WIDTH * 0.04, txt_color, center=False))
        self.guide_texts.append(self.create_text("*at Settings there's a green arrow for next page", consts.WIN_WIDTH / 100,consts.WIN_HEIGHT * 0.8, consts.WIN_WIDTH * 0.04, txt_color, center=False))

        self.back_text = self.create_text("Back", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT * 0.925, consts.WIN_WIDTH * 0.1,consts.RED)

        while self.in_guide == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.is_click_on_rect(self.back_text[1]):
                        self.in_guide = False
                        self.in_menu = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.draw.rect(self.win, consts.LIGHT_BLUE, pygame.Rect(0, 0, consts.WIN_WIDTH, consts.WIN_WIDTH))
            self.win.blit(self.GuideTitleText[0], self.GuideTitleText[1])
            for txt in self.guide_texts:
                self.win.blit(txt[0], txt[1])
            self.win.blit(self.back_text[0], self.back_text[1])
            pygame.display.update()

    def game_settings(self):
        self.SettingsTitleText = self.create_text("Settings", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT / 8,consts.WIN_WIDTH / 8, consts.PURPLE)

        # Setting Page 1
        self.BattleModeTitleText = self.create_text("BattleMode:", consts.WIN_WIDTH*0.5, consts.WIN_HEIGHT*0.3 ,consts.WIN_WIDTH*0.1, consts.LIGHT_BLUE_V2)
        self.BattleModeText = self.create_text("%s" % self.BattleMode[self.ModeLevel1][self.ModeLevel2], consts.WIN_WIDTH*0.5, consts.WIN_HEIGHT*0.42 ,consts.WIN_WIDTH*0.07, consts.GREEN)

        self.DiscsColorsTitle = self.create_text("Discs Colors:", consts.WIN_WIDTH*0.5, consts.WIN_HEIGHT*0.58 ,consts.WIN_WIDTH*0.1, consts.CYAN)
        self.DiscColorText1 = self.create_text(str(self.AllColorsNames[self.DiscColor1]), consts.WIN_WIDTH*0.25, consts.WIN_HEIGHT*0.7 ,consts.WIN_WIDTH*0.1, self.AllColors[self.DiscColor1])
        self.DiscColorText2 = self.create_text(str(self.AllColorsNames[self.DiscColor2]), consts.WIN_WIDTH*0.75, consts.WIN_HEIGHT*0.7 ,consts.WIN_WIDTH*0.1, self.AllColors[self.DiscColor2])
        self.DiscColorMiddleSpace = self.create_text("-", consts.WIN_WIDTH * 0.5,consts.WIN_HEIGHT * 0.7, consts.WIN_WIDTH * 0.2,consts.CYAN)


        # Setting Page 2
        self.DepthBot1Text = self.create_text("Depth Bot1: %s"%self.DepthBot1, consts.WIN_WIDTH*0.5, consts.WIN_HEIGHT*0.3 ,consts.WIN_WIDTH*0.08, self.AllColors[self.DiscColor1])
        self.DepthBot2Text = self.create_text("Depth Bot2: %s"%self.DepthBot2, consts.WIN_WIDTH*0.5, consts.WIN_HEIGHT*0.4 ,consts.WIN_WIDTH*0.08, self.AllColors[self.DiscColor2])
        self.FunnyText = self.create_text("Funny:", consts.WIN_WIDTH*0.4, consts.WIN_HEIGHT*0.5 ,consts.WIN_WIDTH*0.08, consts.BRONZE)
        self.FunnySwitchText = self.create_text("Off", consts.WIN_WIDTH*0.6, consts.WIN_HEIGHT*0.5 ,consts.WIN_WIDTH*0.08, consts.RED)

        self.back_text = self.create_text("Back", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT * 0.9, consts.WIN_WIDTH*0.1,consts.RED)
        self.RightGreenArrow = self.rot_center(consts.Green_Arrow, -90, consts.WIN_WIDTH*0.7, consts.WIN_HEIGHT * 0.9)
        self.LeftGreenArrow = self.rot_center(consts.Green_Arrow, 90, consts.WIN_WIDTH*0.3, consts.WIN_HEIGHT * 0.9)
        DepthCap = 9

        while self.in_settings == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.is_click_on_rect(self.back_text[1]):
                        self.in_settings = False
                        self.in_menu = True
                        self.settings_page=1
                        self.DepthBot1Text = self.create_text("Depth Bot1: %s" % self.DepthBot1, consts.WIN_WIDTH * 0.5,consts.WIN_HEIGHT * 0.3, consts.WIN_WIDTH * 0.08,self.AllColors[self.DiscColor1])
                        self.DepthBot2Text = self.create_text("Depth Bot2: %s" % self.DepthBot2, consts.WIN_WIDTH * 0.5,consts.WIN_HEIGHT * 0.4, consts.WIN_WIDTH * 0.08,self.AllColors[self.DiscColor2])

                    if (self.settings_page == 1):
                        if self.is_click_on_rect(self.RightGreenArrow[1]):
                            self.settings_page += 1
                            self.DepthBot1Text = self.create_text("Depth Bot1: %s" % self.DepthBot1,consts.WIN_WIDTH * 0.5, consts.WIN_HEIGHT * 0.3,consts.WIN_WIDTH * 0.08,self.AllColors[self.DiscColor1])
                            self.DepthBot2Text = self.create_text("Depth Bot2: %s" % self.DepthBot2,consts.WIN_WIDTH * 0.5, consts.WIN_HEIGHT * 0.4,consts.WIN_WIDTH * 0.08,self.AllColors[self.DiscColor2])
                    elif (self.settings_page == 2):
                        if self.is_click_on_rect(self.LeftGreenArrow[1]):
                            self.settings_page -= 1


                    if(self.settings_page==1):
                        if self.is_click_on_rect(self.BattleModeText[1]):
                            if event.button == 1:
                                self.ModeLevel1+=1 if(self.ModeLevel1!=2) else -self.ModeLevel1
                            elif event.button == 3:
                                self.ModeLevel2+=1 if(self.ModeLevel2!=2) else -self.ModeLevel2
                            self.BattleModeText = self.create_text("%s" % self.BattleMode[self.ModeLevel1][self.ModeLevel2],consts.WIN_WIDTH * 0.5, consts.WIN_HEIGHT * 0.42,consts.WIN_WIDTH*0.07, consts.GREEN)

                        if self.is_click_on_rect(self.DiscColorText1[1]):
                            if event.button == 1:
                                self.DiscColor1+=1 if(self.DiscColor1!=len(self.AllColorsNames)-1) else -self.DiscColor1
                            elif event.button == 3:
                                self.DiscColor1-=1 if(self.DiscColor1!=0) else -len(self.AllColorsNames)+1
                            self.DiscColorText1 = self.create_text(str(self.AllColorsNames[self.DiscColor1]),consts.WIN_WIDTH * 0.25, consts.WIN_HEIGHT * 0.7,consts.WIN_WIDTH * 0.1, self.AllColors[self.DiscColor1])

                        if self.is_click_on_rect(self.DiscColorText2[1]):
                            if event.button == 1:
                                self.DiscColor2+=1 if(self.DiscColor2!=len(self.AllColorsNames)-1) else -self.DiscColor2
                            elif event.button == 3:
                                self.DiscColor2-=1 if(self.DiscColor2!=0) else -len(self.AllColorsNames)+1
                            self.DiscColorText2 = self.create_text(str(self.AllColorsNames[self.DiscColor2]),consts.WIN_WIDTH * 0.75, consts.WIN_HEIGHT * 0.7,consts.WIN_WIDTH * 0.1, self.AllColors[self.DiscColor2])
                    elif(self.settings_page==2):
                        if self.is_click_on_rect(self.DepthBot1Text[1]):
                            if event.button == 1:
                                if(self.DepthBot1<DepthCap):
                                    self.DepthBot1 += 1
                            elif event.button == 3:
                                if(self.DepthBot1>1):
                                    self.DepthBot1 -= 1
                            self.DepthBot1Text = self.create_text("Depth Bot1: %s" % self.DepthBot1,consts.WIN_WIDTH * 0.5,consts.WIN_HEIGHT * 0.3,consts.WIN_WIDTH * 0.08,self.AllColors[self.DiscColor1])


                        if self.is_click_on_rect(self.DepthBot2Text[1]):
                            if event.button == 1:
                                if(self.DepthBot2<DepthCap):
                                    self.DepthBot2 += 1
                            elif event.button == 3:
                                if(self.DepthBot2>1):
                                    self.DepthBot2 -= 1
                            self.DepthBot2Text = self.create_text("Depth Bot2: %s" % self.DepthBot2,consts.WIN_WIDTH * 0.5, consts.WIN_HEIGHT * 0.4,consts.WIN_WIDTH * 0.08,self.AllColors[self.DiscColor2])

                        if self.is_click_on_rect(self.FunnySwitchText[1]):
                            if(self.Funny):
                                self.FunnySwitchText = self.create_text("Off", consts.WIN_WIDTH * 0.6,consts.WIN_HEIGHT * 0.5,consts.WIN_WIDTH * 0.08, consts.RED)
                                self.Funny=False
                            else:
                                self.FunnySwitchText = self.create_text("On", consts.WIN_WIDTH * 0.6,consts.WIN_HEIGHT * 0.5,consts.WIN_WIDTH * 0.08, consts.GREEN)
                                self.Funny = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.draw.rect(self.win, consts.LIGHT_BLUE, pygame.Rect(0, 0, consts.WIN_WIDTH, consts.WIN_WIDTH))
            self.win.blit(self.SettingsTitleText[0], self.SettingsTitleText[1])
            if(self.settings_page==1):
                self.win.blit(self.BattleModeTitleText[0], self.BattleModeTitleText[1])
                self.win.blit(self.BattleModeText[0], self.BattleModeText[1])
                self.win.blit(self.DiscsColorsTitle[0], self.DiscsColorsTitle[1])
                self.win.blit(self.DiscColorText1[0], self.DiscColorText1[1])
                self.win.blit(self.DiscColorText2[0], self.DiscColorText2[1])
                self.win.blit(self.DiscColorMiddleSpace[0], self.DiscColorMiddleSpace[1])
            elif(self.settings_page==2):
                self.win.blit(self.DepthBot1Text[0], self.DepthBot1Text[1])
                self.win.blit(self.DepthBot2Text[0], self.DepthBot2Text[1])
                self.win.blit(self.FunnyText[0],self.FunnyText[1])
                self.win.blit(self.FunnySwitchText[0],self.FunnySwitchText[1])


            self.win.blit(self.back_text[0], self.back_text[1])
            if(self.settings_page==1):
                self.win.blit(self.RightGreenArrow[0],self.RightGreenArrow[1])
            elif(self.settings_page==2):
                self.win.blit(self.LeftGreenArrow[0], self.LeftGreenArrow[1])

            pygame.display.update()
            clock.tick(15)

    def game_menu(self):
        self.GameNameText = self.create_text("Connect Four AI", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT*0.1,consts.WIN_WIDTH*0.12, consts.ORANGE)
        self.StartText = self.create_text("Start", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT*0.3 ,consts.WIN_WIDTH*0.135, consts.LIGHT_GREEN)
        self.SettingsText = self.create_text("Settings", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT*0.5 ,consts.WIN_WIDTH*0.13, consts.PURPLE)
        self.GuideText = self.create_text("Guide", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT * 0.7,consts.WIN_WIDTH * 0.13, consts.GOLD)
        self.QuitText = self.create_text("Quit", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT*0.9 ,consts.WIN_WIDTH*0.13, consts.RED)


        while self.in_menu:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.is_click_on_rect(self.StartText[1]):
                        self.in_menu = False

                    if self.is_click_on_rect(self.SettingsText[1]):
                        self.in_settings = True
                        self.in_menu = False

                    if self.is_click_on_rect(self.GuideText[1]):
                        self.in_guide = True
                        self.in_menu = False

                    if self.is_click_on_rect(self.QuitText[1]):
                        pygame.quit()
                        quit()


            pygame.draw.rect(self.win, consts.LIGHT_BLUE, pygame.Rect(0, 0, consts.WIN_WIDTH, consts.WIN_WIDTH))
            self.win.blit(self.GameNameText[0], self.GameNameText[1])
            self.win.blit(self.StartText[0], self.StartText[1])
            self.win.blit(self.SettingsText[0], self.SettingsText[1])
            self.win.blit(self.GuideText[0], self.GuideText[1])
            self.win.blit(self.QuitText[0], self.QuitText[1])
            pygame.display.update()