# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Selenium Classes Data Elements Module
"""


class AbstractElementData:
    path: str = "/"


class QRCode(AbstractElementData):
    """Representa o elemento de QR Code na página de autenticação."""
    path: str = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas"


class SearchEdit(AbstractElementData):
    """Representa o elemento de pesquisa de contatos e grupos."""
    path: str = "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div"


class SearchClearButton(AbstractElementData):
    """Botão para limpar a pesquisa de contatos."""
    path: str = "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/span/button"


class SendMessage(AbstractElementData):
    """Representa o elemento de envio de mensagem de um contato ou grupo."""
    path: str = "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]"


class Group(AbstractElementData):
    """Representa o elemento de título de grupo."""
    path: str = "/html/body/div/div/div/div[3]/header/div[1]/div/span/img"


class GroupMenuButton(AbstractElementData):
    """Representa o botão de menu do grupo."""
    path: str = "/html/body/div[1]/div/div[2]/div[4]/div/header/div[2]"


class GroupEditButton(AbstractElementData):
    """Representa o botão de edição do título do grupo."""
    path: str = ('/html/body/div[1]/div/div[2]/div[5]/span/div/span/div/div/div/section/div[1]/div/div[2]/div/div/'
                 'span[2]/button')


class GroupNameEdit(AbstractElementData):
    """Representa o elemento de edição do nome do grupo."""
    path: str = '/html/body/div/div/div/div[2]/div[3]/span/div/span/div/div/section/div[1]/div[2]/div[1]/div/div[2]'


class GroupClosePanelButton(AbstractElementData):
    """Representa o botão de fechar painel do grupo."""
    path: str = '/html/body/div[1]/div/div[2]/div[5]/span/div/span/div/div/header/div/div[1]/div'


class ParticipantsSelector(AbstractElementData):
    """Representa o seletor de participantes."""
    path: str = ("/html/body/div[1]/div/div[2]/div[5]/span/div/span/div/div/div/section/div[1]/div/div[3]"
                 "/span/span/button")


class GroupMore(AbstractElementData):
    """Representa o elemento de mais opções do grupo."""
    path: str = '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span'


class NewGroupButton(AbstractElementData):
    """Representa o botão de novo grupo."""
    path: str = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div'


class GroupContactName(AbstractElementData):
    """Representa o nome do contato do grupo."""
    path: str = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input'


class CreateGroupNextStep(AbstractElementData):
    """Representa o botão de próximo passo na criação do grupo."""
    path: str = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span'


class CreateGroupEdit(AbstractElementData):
    """Representa o elemento de edição na criação do grupo."""
    path: str = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]'


class MainMenu(AbstractElementData):
    """Representa o menu principal."""
    path: str = "#main > header > div._1WBXd > div._2EbF- > div > span"


class ChatMenu(AbstractElementData):
    """Representa o menu de chat."""
    path: str = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/div/span"


class GroupMenu(AbstractElementData):
    """Representa o menu do grupo."""
    path: str = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div"


class GroupDataButton(AbstractElementData):
    """Representa o botão de dados do grupo."""
    path: str = '/html/body/div/div[1]/span[4]/div/ul/div/div/li[1]'


class GroupLinkButton(AbstractElementData):
    """Representa o botão de link do grupo."""
    path: str = '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[3]'


class GroupInviteLinkAnchor(AbstractElementData):
    """Representa o link de convite do grupo."""
    path: str = '/html/body/div/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[2]/div/span'


class GroupInfo(AbstractElementData):
    """Representa as informações do grupo."""
    path: str = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/span/div/ul/li[1]/div'


class GroupImageButton(AbstractElementData):
    """Representa o botão de imagem do grupo."""
    path: str = '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[1]/div[1]/div/input'


class GroupCreateImageButton(AbstractElementData):
    """Representa o botão de criar imagem do grupo."""
    path: str = '/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[1]/div/input'


class GroupLoadPhoto(AbstractElementData):
    """Representa o elemento de carregar foto do grupo."""
    path: str = '#app > div > span:nth-child(4) > div > ul > li:nth-child(2) > div'


class GroupImageInput(AbstractElementData):
    """Representa o campo de entrada de imagem do grupo."""
    path: str = '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[1]/div/input'


class GroupZoomOut(AbstractElementData):
    """Representa o elemento de zoom out do grupo."""
    path: str = '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[1]/div[1]/div[2]'


class GroupImageSaveButton(AbstractElementData):
    """Representa o botão de salvar imagem do grupo."""
    path: str = '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div/span'


class GroupExitInfo(AbstractElementData):
    """Representa o elemento de sair das informações do grupo."""
    path: str = '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[1]/button'


class GroupJoinChat(AbstractElementData):
    """Representa o elemento de entrar no chat do grupo."""
    path: str = "#action-button"


class GroupJoin(AbstractElementData):
    """Representa o elemento de entrar no grupo."""
    path: str = '//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[2]/div[2]'


class GroupLeave(AbstractElementData):
    """Representa o elemento de sair do grupo."""
    path: str = '//*[@id="main"]/header/div[3]/div/div[3]/span/div/ul/li[5]/div'


class GroupLeaveButton(AbstractElementData):
    """Representa o botão de sair do grupo."""
    path: str = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]'


class GroupSettings(AbstractElementData):
    """Representa as configurações do grupo."""
    path: str = '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[4]/div[4]'


class GroupSettingsSendMessages(AbstractElementData):
    """Representa as configurações de envio de mensagens do grupo."""
    path: str = '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/div[3]/div'


class GroupSettingsSendMessagesAllParticipants(AbstractElementData):
    """Representa a configuração de envio de mensagens para todos os participantes do grupo."""
    path: str = '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/form/ol/li[1]/label'


class GroupSettingsSendMessagesOnlyAdmins(AbstractElementData):
    """Representa a configuração de envio de mensagens apenas para administradores do grupo."""
    path: str = '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/form/ol/li[2]/label'


class GroupSettingsSendMessagesConfirmButton(AbstractElementData):
    """Representa o botão de confirmação das configurações de envio de mensagens do grupo."""
    path: str = '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[3]/div[2]'


class GroupSettingsEditGroupData(AbstractElementData):
    """Representa as configurações de edição de dados do grupo."""
    path: str = '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/div[1]/div'


class GroupSettingsEditGroupDataOnlyAdmins(AbstractElementData):
    """Representa a configuração de edição de dados do grupo apenas para administradores."""
    path: str = '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/form/ol/li[2]/label'


class GroupSettingsEditGroupDataConfirmButton(AbstractElementData):
    """Representa o botão de confirmação das configurações de edição de dados do grupo."""
    path: str = '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[3]/div[2]'


class GroupSettingsExitButton(AbstractElementData):
    """Representa o botão de sair das configurações do grupo."""
    path: str = '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[1]/button'


class ScrollBar(AbstractElementData):
    """Representa a barra de rolagem."""
    path: str = "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div"


class Participant1(AbstractElementData):
    """Representa o participante 1."""
    path: str = '_3TEwt'


class Participant2(AbstractElementData):
    """Representa o participante 2."""
    path: str = '_25Ooe'


class Participant3(AbstractElementData):
    """Representa o participante 3."""
    path: str = '_1wjpf'


class StatusCssSelector(AbstractElementData):
    """Representa o seletor CSS do status."""
    path: str = ".drawer-section-body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"


class LastSeen(AbstractElementData):
    """Representa o elemento de última visualização."""
    path: str = '._315-i'


class Attach(AbstractElementData):
    """Representa o elemento de anexo."""
    path: str = '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/div'


class SendFile(AbstractElementData):
    """Representa o elemento de envio de arquivo."""
    path: str = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span'


class PictureAttachType(AbstractElementData):
    """Representa o tipo de anexo de imagem."""
    path: str = '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input'


class DocumentAttachType(AbstractElementData):
    """Representa o tipo de anexo de documento."""
    path: str = '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[3]/button/input'


class SendDocumentAttachButton(AbstractElementData):
    """Representa o botão de envio de anexo de documento."""
    path: str = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div'


class PictureCaption(AbstractElementData):
    """Representa a legenda da imagem."""
    path: str = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]/div[2]"


class ClearChat(AbstractElementData):
    """Representa o elemento de limpar o chat."""
    path: str = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]'


class OpenProfile(AbstractElementData):
    """Representa o elemento de abrir o perfil."""
    path: str = "/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img"


class OpenProfilePicture(AbstractElementData):
    """Representa o elemento de abrir a imagem do perfil."""
    path: str = "/html/body/div[1]/div/div/div[1]/div[3]/span/div/span/div/div/div/div[1]/div[1]/div/img"


class ProfileImage(AbstractElementData):
    """Representa a imagem do perfil."""
    path: str = '//*[@id="app"]/div/span[2]/div/div/div[2]/div/div/div/div/img'
