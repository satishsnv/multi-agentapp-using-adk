from agents.models import FileContent
import re

async def fetch_file_content(file_id: str) -> str:
    """Fetch content for the specified file resource ID in the FileContent format.

    Args:
        file_id (str): The ID of the file to fetch content for.

    Returns:
        FileContent: list of file content items, along with file_id.
    """

    # Simulate fetching file content
    # In a real implementation, this would read the file from storage
    print(f"Fetching content for file ID: {file_id}")

    
    result = FileContent()
    result.file_id = file_id
    result.file_content.append(re.sub(r'\s+', ' ', """
            I was born in the northern part of this united kingdom, in the house of my grandfather, a gentleman of considerable fortune and influence, who
            had on many occasions signalised himself in behalf of his country; and was remarkable for his abilities in the law, which he exercised with
            great success in the station of a judge, particularly against beggars,for whom he had a singular aversion.

            My father (his youngest son) falling in love with a poor relation, who
            lived with the old gentleman in quality of a housekeeper, espoused her
            privately; and I was the first fruit of that marriage. During her
            pregnancy, a dream discomposed my mother so much that her husband,
            tired with her importunity, at last consulted a highland seer, whose
            favourable interpretation he would have secured beforehand by a bribe,
            but found him incorruptible. She dreamed she was delivered of a
            tennis-ball, which the devil (who, to her great surprise, acted the
            part of a midwife) struck so forcibly with a racket that it disappeared
            in an instant; and she was for some time inconsolable for the lost of
            her offspring; when, all on a sudden, she beheld it return with equal
            violence, and enter the earth, beneath her feet, whence immediately
            sprang up a goodly tree covered with blossoms, the scent of which
            operated so strongly on her nerves that she awoke. The attentive sage,
            after some deliberation, assured my parents, that their firstborn would
            be a great traveller; that he would undergo many dangers and
            difficulties, and at last return to his native land, where he would
            flourish in happiness and reputation. How truly this was foretold will
            appear in the sequel. It was not long before some officious person
            informed my grandfather of certain familiarities that passed between
            his son and housekeeper which alarmed him so much that, a few days
            after, he told my father it was high time for him to think of settling;
            and that he had provided a match for him, to which he could in justice
            have no objections. My father, finding it would be impossible to
            conceal his situation much longer, frankly owned what he had done; and
            excused himself for not having asked the consent of his father, by
            saying, he knew it would have been to no purpose; and that, had his
            inclination been known, my grandfather might have taken such measures
            as would have effectually put the gratification of it out of his power:
            he added, that no exceptions could be taken to his wife’s virtue,
            birth, beauty, and good sense, and as for fortune, it was beneath his
            care. The old gentleman, who kept all his passions, except one, in
            excellent order, heard him to an end with great temper, and then calmly
            asked, how he proposed to maintain himself and spouse? He replied, he
            could be in no danger of wanting while his father’s tenderness
            remained, which he and his wife should always cultivate with the utmost
            veneration; and he was persuaded his allowance would be suitable to the
            dignity and circumstances of his family, and to the provision already
            made for his brothers and sisters, who were happily settled under his
            protection. “Your brothers and sisters,” said my grandfather, “did not
            think it beneath them to consult me in an affair of such importance as
            matrimony; neither, I suppose, would you have omitted that piece of
            duty, had you not some secret fund in reserve; to the comforts of which
            I leave you, with a desire that you will this night seek out another
            habitation for yourself and wife, whither, in a short time, I will send
            you an account of the expense I have been at in your education, with a
            view of being reimbursed. Sir, you have made the grand tour—you are a
            polite gentleman—a very pretty gentleman—I wish you a great deal of
            joy, and am your very humble servant.""").strip())

    result.file_content.append(re.sub(r'\s+', ' ', """So saying, he left my father in a situation easily imagined. However,
            he did not long hesitate; for, being perfectly well acquainted with his
            father’s disposition, he did not doubt that he was glad of this
            pretence to get rid of him; and his resolves being as invariable as the
            laws of the Medes and Persians, he knew it would be to no purpose to
            attempt him by prayers and entreaties; so without any farther
            application, he betook himself, with his disconsolate bedfellow to a
            farm-house, where an old servant of his mother dwelt: there they
            remained some time in a situation but ill adapted to the elegance of
            their desires and tenderness of their love; which nevertheless my
            father chose to endure, rather than supplicate an unnatural and
            inflexible parent but my mother, foreseeing the inconveniences to which
            she must have been exposed, had she been delivered in this place (and
            her pregnancy was very far advanced), without communicating her design
            to her husband, went in disguise to the house of my grandfather, hoping
            that her tears and condition would move him to compassion, and
            reconcile him to an event which was now irrecoverably past.

            She found means to deceive the servants, and get introduced as an
            unfortunate lady, who wanted to complain of some matrimonial
            grievances, it being my grandfather’s particular province to decide in
            all cases of scandal. She was accordingly admitted into his presence,
            where, discovering herself, she fell at his feet, and in the most
            affecting manner implored his forgiveness; at the same time
            representing the danger that threatened not only her life, but that of
            his own grandchild, which was about to see the light. He told her he
            was sorry that the indiscretion of her and his son had compelled him to
            make a vow, which put it out of his power to give them any assistance;
            that he had already imparted his thoughts on that subject to her
            husband, and was surprised that they should disturb his peace with any
            farther importunity. This said, he retired.""").strip())

    result.file_content.append(re.sub(r'\s+', ' ', """The violence of my mother’s affliction had such an effect on her
            constitution that she was immediately seized with the pains of
            childbed; and had not an old maidservant, to whom she was very dear,
            afforded her pity and assistance, at the hazard of incurring my
            grandfather’s displeasure, she and the innocent fruit of her womb must
            have fallen miserable victims to his rigour and inhumanity. By the
            friendship of this poor woman she was carried up to a garret, and
            immediately delivered of a man child, the story of whose unfortunate
            birth he himself now relates. My father, being informed of what had
            happened, flew to the embraces of his darling spouse, and while he
            loaded his offspring with paternal embraces, could not forbear shedding
            a flood of tears on beholding the dear partner of his heart (for whose
            ease he would have sacrificed the treasures of the east) stretched upon
            a flock bed, in a miserable apartment, unable to protect her from the
            inclemencies of the weather. It is not to be supposed that the old
            gentleman was ignorant of what passed, though he affected to know
            nothing of the matter, and pretended to be very much surprised, when
            one of his grandchildren, by his eldest son deceased, who lived with
            him as his heir apparent, acquainted him with the affair; he determined
            therefore to observe no medium, but immediately (on the third day after
            her delivery) sent her a peremptory order to be gone, and turned off
            the servant who had preserved her life. This behaviour so exasperated
            my father that he had recourse to the most dreadful imprecations; and
            on his bare knees implored that Heaven would renounce him if ever he
            should forget or forgive the barbarity of his sire.

            The injuries which this unhappy mother received from her removal in
            such circumstances, and the want of necessaries where she lodged,
            together with her grief and anxiety of mind, soon threw her into a
            languishing disorder, which put an end to her life. My father, who
            loved her tenderly, was so affected with her death that he remained six
            weeks deprived of his senses; during which time, the people where he
            lodged carried the infant to the old man who relented so far, on
            hearing the melancholy story of his daughter-in-law’s death, and the
            deplorable condition of his son, as to send the child to nurse, and he
            ordered my father to be carried home to his house, where he soon
            recovered the use of his reason.

            Whether this hardhearted judge felt any remorse for his cruel treatment
            of his son and daughter, or (which is more probable) was afraid his
            character would suffer in the neighbourhood, he professed great sorrow
            for his conduct to my father, whose delirium was succeeded by a
            profound melancholy and reserve. At length he disappeared, and,
            notwithstanding all imaginable inquiry, could not be heard of; a
            circumstance which confirmed most people in the opinion of his having
            made away with himself in a fit of despair. How I understood the
            particulars of my birth will appear in the course of these memoirs.""").strip())
    
     

    return result.model_dump_json()

